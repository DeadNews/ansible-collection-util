#!/usr/bin/env python3
"""An Ansible module that uses either copy or template based on the source file extension."""

from ansible.module_utils.basic import AnsibleModule
from ansible.plugins.action.copy import ActionModule as CopyActionModule
from ansible.plugins.action.template import ActionModule as TemplateActionModule

DOCUMENTATION = r"""
---
module: copy_or_tpl
short_description: This module copies a file or renders a template based on the source file extension
description:
    - This Ansible module checks the extension of the source file.
        If it ends with '.j2', it uses ansible.builtin.template to render the file as a Jinja2 template.
        Otherwise, it uses ansible.builtin.copy to copy the file as is.
options:
    src:
        description:
            - The local path to the file to copy or render.
        required: true
        type: str
    dest:
        description:
            - The remote path where the file should be copied to.
        required: true
        type: str
    mode:
        description:
            - The permissions to set on the file.
        type: str
"""

EXAMPLES = r"""
# Copy a file
- name: Test copy_or_tpl module with a file
    deadnews.util.copy_or_tpl:
        src: /path/to/file.txt
        dest: /remote/path/to/file.txt

# Render a template
- name: Test copy_or_tpl module with a template
    deadnews.util.copy_or_tpl:
        src: /path/to/template.j2
        dest: /remote/path/to/template.txt
"""

RETURN = r"""
dest:
    description: Destination path on the remote host.
    returned: success
    type: str
    sample: /path/to/file.txt
src:
    description: Source file used for the copy or template operation.
    returned: success
    type: str
    sample: /path/to/source.txt
"""


def main() -> None:
    """The main function for the Ansible module."""
    module = AnsibleModule(
        argument_spec={
            "src": {"type": "path", "required": True},
            "dest": {"type": "path", "required": True},
            "mode": {"type": "raw"},
        },
        supports_check_mode=True,
    )

    src = module.params["src"]
    dest = module.params["dest"]
    mode = module.params["mode"]

    action_module = (
        TemplateActionModule(module._module)  # noqa: SLF001
        if src.endswith(".j2")
        else CopyActionModule(module._module)  # noqa: SLF001
    )

    result = action_module.run(
        task_vars={
            "src": src,
            "dest": dest,
            "mode": mode,
        }
    )

    if result.get("failed"):
        module.fail_json(msg=result.get("msg", ""))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
