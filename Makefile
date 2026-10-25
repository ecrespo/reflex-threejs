.PHONY: help install stubs lint test check build clean publish

help:  ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  %-10s %s\n", $$1, $$2}'

install:  ## Install the package and dev tooling in editable mode.
	pip install -e ".[dev]"

stubs:  ## Regenerate the .pyi type stubs for the component package.
	python scripts/gen_pyi.py

lint:  ## Run ruff over the repo.
	ruff check .

test:  ## Run the test suite.
	pytest -q

check: lint test  ## Lint and test.

build: stubs  ## Regenerate stubs, then build the wheel + sdist.
	python -m build
	python -m twine check dist/*

clean:  ## Remove build artifacts.
	rm -rf dist build

publish: build  ## Manual upload to PyPI (releases normally go through the tag-triggered workflow).
	python -m twine upload dist/*
