# deadnews.util.wireguard

> Setup Wireguard

## Role Variables

- [meta/argument_specs.yml](./meta/argument_specs.yml)
- [vars/main.yml](./vars/main.yml)

## Example Playbook

- [molecule/wireguard/converge.yml](./molecule/wireguard/converge.yml)

```yaml
- hosts: servers
  roles:
    - role: deadnews.util.wireguard
      wireguard_interface: wg0
      wireguard_template: templates/wg0.conf.j2
```
