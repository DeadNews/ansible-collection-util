#!/usr/bin/env python3
"""An Ansible module to enable/disable linger for a user."""

import subprocess
from pathlib import Path
from shutil import which

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = r"""
---
module: linger
short_description: This module enables or disables linger for a user
description:
    - This Ansible module enables or disables linger for a user using loginctl.
options:
    user:
        description:
            - The user for which to enable or disable linger.
        required: true
        type: str
    state:
        description:
            - The desired state for linger. Can be either "present" or "absent".
        required: true
        type: str
"""

EXAMPLES = r"""
# Enable linger for a user
- name: Enable linger for user
    deadnews.util.linger:
        user: myuser
        state: present

# Disable linger for a user
- name: Disable linger for user
    deadnews.util.linger:
        user: myuser
        state: absent
"""

RETURN = r"""
message:
    description: A message indicating what changes were made.
    type: str
    returned: always
changed:
    description: A boolean indicating if any changes were made.
    type: bool
    returned: always
"""


def main() -> None:
    """The main function for the Ansible module."""
    argument_spec = {
        "user": {"type": "str", "required": True},
        "state": {"type": "str", "choices": ["present", "absent"], "required": True},
    }

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    result = {"changed": False, "message": ""}

    if module.check_mode:
        module.exit_json(**result)

    user = module.params["user"]
    state = module.params["state"]

    linger_exists = Path(f"/var/lib/systemd/linger/{user}").is_file()

    if (state == "present" and linger_exists) or (state == "absent" and not linger_exists):
        module.exit_json(**result)

    loginctl = which("loginctl")
    if not loginctl:
        module.fail_json(msg="loginctl is not found on the system.", **result)
        return

    if state == "present":
        subprocess.call([loginctl, "enable-linger", user])
        result["changed"] = True
        result["message"] = f"Linger has been enabled for {user}"
    else:
        subprocess.call([loginctl, "disable-linger", user])
        result["changed"] = True
        result["message"] = f"Linger has been disabled for {user}"

    module.exit_json(**result)


if __name__ == "__main__":
    main()
