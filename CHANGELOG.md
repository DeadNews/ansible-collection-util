# Changelog

## [1.7.1](https://github.com/DeadNews/ansible-collection-util/compare/v1.7.0...v1.7.1) - 2025-02-03

### 🚀 Features

- _(aptup)_ add option to auto restart services during upgrades ([#85](https://github.com/DeadNews/ansible-collection-util/issues/85)) - ([b529c36](https://github.com/DeadNews/ansible-collection-util/commit/b529c3611704c0b2b7489f35bb3c33b43c24fcec))

### ⬆️ Dependencies

- _(deps)_ update dependency ansible-core to v2.18.2 ([#83](https://github.com/DeadNews/ansible-collection-util/issues/83)) - ([d169a9e](https://github.com/DeadNews/ansible-collection-util/commit/d169a9e7eef14256fbbe6e0acc761aeac7421525))

## [1.7.0](https://github.com/DeadNews/ansible-collection-util/compare/v1.6.7...v1.7.0) - 2025-01-31

### 🚀 Features

- _(aptup)_ explicitly tell to only list the services that need to be restarted ([#82](https://github.com/DeadNews/ansible-collection-util/issues/82)) - ([c7fef04](https://github.com/DeadNews/ansible-collection-util/commit/c7fef040b336b1c4ded4987abdd15d05fa0faddf))

### 🧹 Chores

- _(config)_ migrate config .renovaterc.json ([#68](https://github.com/DeadNews/ansible-collection-util/issues/68)) - ([301c19d](https://github.com/DeadNews/ansible-collection-util/commit/301c19d56c0dd7743cf9743f1131fdc647bf4307))

### ⬆️ Dependencies

- _(deps)_ update dependencies - ([bbf5e97](https://github.com/DeadNews/ansible-collection-util/commit/bbf5e972f46bed7811cac58917ed198785b9f864))
- _(deps)_ update dependency ansible-core to v2.18.1 ([#74](https://github.com/DeadNews/ansible-collection-util/issues/74)) - ([211ab09](https://github.com/DeadNews/ansible-collection-util/commit/211ab09318b64db86825e588cc66cb7f68cd5ba7))
- _(deps)_ bump minimal version to `python:3:12` - ([395add7](https://github.com/DeadNews/ansible-collection-util/commit/395add7ae83a64eaa25832ef41d6de02f7709f79))
- _(deps)_ update dependency ansible-core to v2.18.0 ([#69](https://github.com/DeadNews/ansible-collection-util/issues/69)) - ([b36b163](https://github.com/DeadNews/ansible-collection-util/commit/b36b16309282d2691ee935509a472cbd3dc3abba))
- _(deps)_ update dependencies ([#67](https://github.com/DeadNews/ansible-collection-util/issues/67)) - ([b0669e3](https://github.com/DeadNews/ansible-collection-util/commit/b0669e3af80b447a31d8f8b1ed682157a57806c4))
- _(deps)_ update dependency ansible-core to v2.17.5 ([#62](https://github.com/DeadNews/ansible-collection-util/issues/62)) - ([37aded8](https://github.com/DeadNews/ansible-collection-util/commit/37aded82c61fbaced2ffc51894afe0027c2542c0))

### ◀️ Revert

- "fix(deps): update dependencies" - ([53c9072](https://github.com/DeadNews/ansible-collection-util/commit/53c9072bb19db11203a5e72409a72eb08ac7337c))

## [1.6.7](https://github.com/DeadNews/ansible-collection-util/compare/v1.6.6...v1.6.7) - 2024-09-12

### 🐛 Bug fixes

- _(docker)_ update uninstall option ([#55](https://github.com/DeadNews/ansible-collection-util/issues/55)) - ([2b55775](https://github.com/DeadNews/ansible-collection-util/commit/2b557756384061fba45d369301da17f2b708ee45))

## [1.6.6](https://github.com/DeadNews/ansible-collection-util/compare/v1.6.5...v1.6.6) - 2024-09-11

### 🚀 Features

- _(docker)_ add uninstall option ([#54](https://github.com/DeadNews/ansible-collection-util/issues/54)) - ([7a3573c](https://github.com/DeadNews/ansible-collection-util/commit/7a3573ca4a442c7ecdf8b63cc1a7e9d00326a6c9))

### ⬆️ Dependencies

- _(deps)_ update dependency ansible-core to v2.17.4 ([#52](https://github.com/DeadNews/ansible-collection-util/issues/52)) - ([2d1d8ce](https://github.com/DeadNews/ansible-collection-util/commit/2d1d8ceb27b2e7c5107c2480b7dd4153b7ea7aa3))
- _(deps)_ update dependency ansible-core to v2.17.3 ([#47](https://github.com/DeadNews/ansible-collection-util/issues/47)) - ([02bee81](https://github.com/DeadNews/ansible-collection-util/commit/02bee81eb87f6075e11298b667eff515a9d4351a))

## [1.6.5](https://github.com/DeadNews/ansible-collection-util/compare/v1.6.4...v1.6.5) - 2024-08-15

### 🐛 Bug fixes

- _(docker)_ update `cleanup_scheduled_until` to 30 days - ([8313a9f](https://github.com/DeadNews/ansible-collection-util/commit/8313a9f5f7b8bdea55233246932b450c89464d71))
- _(docker_compose)_ change default permissions from `0600` to `0644` on created files - ([ade785a](https://github.com/DeadNews/ansible-collection-util/commit/ade785a11b5166be60f791e95de6ce4cf7bf0aa2))

### ⬆️ Dependencies

- _(deps)_ update dependency ansible-core to v2.17.2 ([#42](https://github.com/DeadNews/ansible-collection-util/issues/42)) - ([9063458](https://github.com/DeadNews/ansible-collection-util/commit/906345882c10b4b240a22e9a247fbca77777d473))

## [1.6.4](https://github.com/DeadNews/ansible-collection-util/compare/v1.6.3...v1.6.4) - 2024-07-15

### 🐛 Bug fixes

- _(docker)_ add `docker_cleanup_scheduled_until` argument ([#41](https://github.com/DeadNews/ansible-collection-util/issues/41)) - ([068b786](https://github.com/DeadNews/ansible-collection-util/commit/068b786a6c9da313d97a3b85e532d04840be9a58))

## [1.6.3](https://github.com/DeadNews/ansible-collection-util/compare/v1.6.2...v1.6.3) - 2024-07-13

### 🐛 Bug fixes

- _(docker_compose)_ add `containers_check_retries` argument ([#40](https://github.com/DeadNews/ansible-collection-util/issues/40)) - ([558e81d](https://github.com/DeadNews/ansible-collection-util/commit/558e81d44050a325f7fd4dc4e334362d42861e1f))

## [1.6.2](https://github.com/DeadNews/ansible-collection-util/compare/v1.6.1...v1.6.2) - 2024-06-29

### 🚀 Features

- _(system_info)_ add role ([#37](https://github.com/DeadNews/ansible-collection-util/issues/37)) - ([895ee00](https://github.com/DeadNews/ansible-collection-util/commit/895ee00f6cf849ab6defa3d3a405daa00339bd63))

## [1.6.1](https://github.com/DeadNews/ansible-collection-util/compare/v1.6.0...v1.6.1) - 2024-06-27

### 🐛 Bug fixes

- _(docker_compose)_ add `directory_mode` option ([#34](https://github.com/DeadNews/ansible-collection-util/issues/34)) - ([095bd11](https://github.com/DeadNews/ansible-collection-util/commit/095bd112d1fe986bbaabb60ae2554338dffa0a0a))

## [1.6.0](https://github.com/DeadNews/ansible-collection-util/compare/v1.5.0...v1.6.0) - 2024-06-22

### 🚀 Features

- _(wireguard)_ add role ([#32](https://github.com/DeadNews/ansible-collection-util/issues/32)) - ([c9be46d](https://github.com/DeadNews/ansible-collection-util/commit/c9be46d4be1ad197099d91d33ada7c1f9b9e5deb))

## [1.5.0](https://github.com/DeadNews/ansible-collection-util/compare/v1.4.2...v1.5.0) - 2024-06-15

### 🚀 Features

- _(docker_compose)_ `healthy_verify` to `containers_check` ([#30](https://github.com/DeadNews/ansible-collection-util/issues/30)) - ([4224d58](https://github.com/DeadNews/ansible-collection-util/commit/4224d58c94448d900006176efb1a178cf8ca0d99))

## [1.4.2](https://github.com/DeadNews/ansible-collection-util/compare/v1.4.1...v1.4.2) - 2024-06-08

### 🐛 Bug fixes

- _(docker_compose)_ rename `docker_compose_show_files` to `docker_compose_files_show` ([#29](https://github.com/DeadNews/ansible-collection-util/issues/29)) - ([114a0fd](https://github.com/DeadNews/ansible-collection-util/commit/114a0fdc4c93932d6dcff607bb45d499cd1b5939))

## [1.4.1](https://github.com/DeadNews/ansible-collection-util/compare/v1.4.0...v1.4.1) - 2024-06-06

### 🐛 Bug fixes

- _(docker_compose)_ remove orphans containers on `down` ([#28](https://github.com/DeadNews/ansible-collection-util/issues/28)) - ([4d8a7cf](https://github.com/DeadNews/ansible-collection-util/commit/4d8a7cf8bcdee42e1081c65b2a025fb17528c167))

## [1.4.0](https://github.com/DeadNews/ansible-collection-util/compare/v1.3.0...v1.4.0) - 2024-05-24

### 🚀 Features

- _(docker_compose)_ add option to remove project ([#23](https://github.com/DeadNews/ansible-collection-util/issues/23)) - ([2d29899](https://github.com/DeadNews/ansible-collection-util/commit/2d298995406adc87a10624d694329c5b1d67b03d))

## [1.3.0](https://github.com/DeadNews/ansible-collection-util/compare/v1.2.2...v1.3.0) - 2024-05-22

### 🚀 Features

- _(docker_compose)_ adjust workflow ([#21](https://github.com/DeadNews/ansible-collection-util/issues/21)) - ([4cafb2f](https://github.com/DeadNews/ansible-collection-util/commit/4cafb2f93adc958bc767228968ea1a24c522c47a))
- _(docker_compose)_ add support for executing commands in containers ([#17](https://github.com/DeadNews/ansible-collection-util/issues/17)) - ([60c361c](https://github.com/DeadNews/ansible-collection-util/commit/60c361ca3a29730cb835068b2e022faf7191768a))

### 🧹 Chores

- _(typos)_ ignore short words - ([80b6147](https://github.com/DeadNews/ansible-collection-util/commit/80b61475056101eeb80a310d5b5bb7d54d049015))

### ⬆️ Dependencies

- _(deps)_ update dependency ansible-core to v2.17.0 ([#18](https://github.com/DeadNews/ansible-collection-util/issues/18)) - ([cc3a8a0](https://github.com/DeadNews/ansible-collection-util/commit/cc3a8a0586f3ad97780b489ee467c4dc4289d150))

## [1.2.2](https://github.com/DeadNews/ansible-collection-util/compare/v1.2.1...v1.2.2) - 2024-05-12

### 🐛 Bug fixes

- _(docker)_ add `user` to generated `cron file` names ([#15](https://github.com/DeadNews/ansible-collection-util/issues/15)) - ([2640ea3](https://github.com/DeadNews/ansible-collection-util/commit/2640ea344a067cf061dd28978cae2ab00fc04dac))

## [1.2.1](https://github.com/DeadNews/ansible-collection-util/compare/v1.2.0...v1.2.1) - 2024-05-06

### 🐛 Bug fixes

- _(docker)_ change `daemon.json` location ([#14](https://github.com/DeadNews/ansible-collection-util/issues/14)) - ([fc47d4b](https://github.com/DeadNews/ansible-collection-util/commit/fc47d4b6775fcf7ef9382f76cf2f098d01293da1))

## [1.2.0](https://github.com/DeadNews/ansible-collection-util/compare/v1.1.0...v1.2.0) - 2024-05-05

### 🚀 Features

- _(docker,docker_compose)_ enhance configs deployment ([#11](https://github.com/DeadNews/ansible-collection-util/issues/11)) - ([5d5fcc8](https://github.com/DeadNews/ansible-collection-util/commit/5d5fcc8ce3705420ae64f415f8cd46d63eb5d938))

## [1.1.0](https://github.com/DeadNews/ansible-collection-util/compare/v1.0.0...v1.1.0) - 2024-04-30

### 🚀 Features

- _(docker,docker_compose)_ enhance configs deployment ([#7](https://github.com/DeadNews/ansible-collection-util/issues/7)) - ([de8341f](https://github.com/DeadNews/ansible-collection-util/commit/de8341fcd1b568ffb2f394ff18fe40427a50949b))

### ⚙️ CI/CD

- _(github)_ update `github-deploy` job ([#3](https://github.com/DeadNews/ansible-collection-util/issues/3)) - ([613147e](https://github.com/DeadNews/ansible-collection-util/commit/613147ebf8ebdef25a5fc73d8fe96e7cf0f6ae06))

### ⬆️ Dependencies

- _(deps)_ update dependency ansible-core to v2.16.6 ([#6](https://github.com/DeadNews/ansible-collection-util/issues/6)) - ([c5a66a7](https://github.com/DeadNews/ansible-collection-util/commit/c5a66a7a48407ba844a7a1ae80ed0abb6cef2069))

## [1.0.0](https://github.com/DeadNews/ansible-collection-util/commits/v1.0.0) - 2024-04-03

### 🚀 Features

- create ansible collection ([#1](https://github.com/DeadNews/ansible-collection-util/issues/1)) - ([9fcc96a](https://github.com/DeadNews/ansible-collection-util/commit/9fcc96a276deabfd1b7987ed3aa1224c02a74ee5))

<!-- generated by git-cliff -->
