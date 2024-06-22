# deadnews.util.docker_compose

> Deploy Docker Compose projects (with docker compose v2)

## Role Variables

- [meta/argument_specs.yml](./meta/argument_specs.yml)
- [vars/main.yml](./vars/main.yml)

## Example Playbook

- [molecule/docker_compose/converge.yml](./molecule/docker_compose/converge.yml)

```yaml
- hosts: servers
  roles:
    - role: deadnews.util.docker_compose
      docker_compose_project: docker-app
      docker_compose_target_dir: ~/docker-compose
      docker_compose_files:
        - src: files/docker-compose.yml
```
