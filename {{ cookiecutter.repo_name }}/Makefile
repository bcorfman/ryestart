PACKAGE := {{ cookiecutter.repo_name }}
PACKAGE_DIR := src/${PACKAGE}
SHELL := env PYTHON_VERSION={{ cookiecutter.python_version}} /bin/bash
.SILENT: run devinstall install test lint format
PYTHON_VERSION ?= {{ cookiecutter.python_version}}

setup:
	curl -LsSf https://astral.sh/uv/install.sh | sh

install:
	uv python pin $(PYTHON_VERSION)
	uv sync --frozen --no-dev

devinstall:
	uv python pin $(PYTHON_VERSION)
	uv sync --all-extras --dev

tools:
	uv tool install ruff
	uv tool install pytest
	uv tool install ipython

test:
	uv tool run pytest

run: 
	uv run python main.py

lint:
	uv tool run ruff check -q --select I --fix  

format:
	uv tool run ruff format

all: devinstall tools lint format test
