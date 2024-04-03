# deadnews.util.docker

> Install Docker on Debian-family OS

## Role Variables

- [meta/argument_specs.yml](./meta/argument_specs.yml)
- [vars/main.yml](./vars/main.yml)

## Example Playbook

- [molecule/docker/converge.yml](./molecule/docker/converge.yml)

```yaml
- hosts: servers
  roles:
    - role: deadnews.util.docker
      docker_rootless: true
```
