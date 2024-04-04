.PHONY: all clean default install lock update checks pc lint test

default: checks

install:
	pre-commit install
	poetry install --sync --no-root
	poetry run ansible-galaxy install -r requirements.yml

lock:
	poetry lock --no-update

update:
	poetry up --latest

checks: pc lint-py

pc:
	pre-commit run -a

lint:
	poetry run ansible-lint

lint-py:
	poetry run poe lint

test-%:
	pushd roles/$* && poetry run molecule test -s $*; popd

test-vg-%:
	pushd roles/$* && poetry run molecule test -s $*_vagrant; popd

bumped:
	git cliff --bumped-version

# make release-tag_name
# make release-$(git cliff --bumped-version)-alpha.0
release-%: checks
	git cliff -o CHANGELOG.md --tag $*
	pre-commit run --files CHANGELOG.md || pre-commit run --files CHANGELOG.md
	git add CHANGELOG.md
	git commit -m "chore(release): prepare for $*"
	git push
	git tag -a $* -m "chore(release): $*"
	git push origin $*
	git tag --verify $*
