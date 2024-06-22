#!/usr/bin/python3
"""A simple Ansible module that returns the message it was given."""

from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = r"""
---
module: hello_world
short_description: This module returns the message it was given
description:
    - This is a simple Ansible module that takes a message as input and returns the same message.
options:
    message:
        description:
            - The message to return.
        required: true
        type: str
"""

EXAMPLES = r"""
# Pass in a message
- name: Test hello_world module
    deadnews.util.hello_world:
        message: "Hello, world!"

# The returned message will be "Hello, world!"
"""

RETURN = r"""
message:
    description: The original message that was passed in.
    type: str
    returned: always
"""


def main() -> None:
    """The main function for the Ansible module."""
    argument_spec = {"message": {"type": "str", "required": True}}

    module = AnsibleModule(argument_spec=argument_spec)

    message = module.params["message"]

    module.exit_json(changed=False, message=message)


if __name__ == "__main__":
    main()
