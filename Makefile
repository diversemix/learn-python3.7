help:
	@echo "Widget Example Makefile"
	@echo "---"

# COMMIT_SLUG = `git log HEAD^..HEAD --pretty=oneline --abbrev-commit | head -c 7`
.DEFAULT_GOAL=help

unit_test: build
	docker-compose up python-test

build:
	docker-compose build
