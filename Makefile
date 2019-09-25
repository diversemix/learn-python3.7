help:
	@echo "Widget Example Makefile"
	@echo "---"

# COMMIT_SLUG = `git log HEAD^..HEAD --pretty=oneline --abbrev-commit | head -c 7`
.DEFAULT_GOAL=help

unit_test: build
	docker-compose up --exit-code-from python-test python-test || (echo "unit_test failed $$?"; exit 1)

build:
	docker-compose build || (echo "build failed $$?"; exit 1)
