.PHONY: all clean default install update checks pc lint test

default: checks

install:
	pre-commit install
	poetry install --sync --no-root
	poetry run ansible-galaxy install -r requirements.yml

update:
	poetry up --latest

checks: pc

pc:
	pre-commit run -a

lint:
	poetry run ansible-lint

test-%:
	pushd roles/$* && poetry run molecule test -s $*; popd

test-vg-%:
	pushd roles/$* && poetry run molecule test -s $*_vagrant; popd

get-next:
	git cliff --bumped-version

# make release-tag_name
# make release-v1.0.0-alpha.0
release-%: checks
	git cliff -o CHANGELOG.md --tag $*
	pre-commit run --files CHANGELOG.md
	git add CHANGELOG.md
	git commit -m "chore(release): prepare for $*"
	git push
	git tag -a $* -m "chore(release): $*"
	git push --tags
	git tag --verify $*
