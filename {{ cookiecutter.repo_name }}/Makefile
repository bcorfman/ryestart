PACKAGE := {{ cookiecutter.repo_name }}
PACKAGE_DIR := src/${PACKAGE}
SHELL := env PYTHON_VERSION={{ cookiecutter.python_version}} /bin/bash
.SILENT: devinstall install test lint format
PYTHON_VERSION ?= {{ cookiecutter.python_version}}

install:
	curl -sSf https://rye-up.com/get | RYE_NO_AUTO_INSTALL=1 RYE_INSTALL_OPTION="--yes" bash
	$(HOME)/.rye/shims/rye sync --no-lock --no-dev

devinstall:
	curl -sSf https://rye-up.com/get | RYE_NO_AUTO_INSTALL=1 RYE_INSTALL_OPTION="--yes" bash
	$(HOME)/.rye/shims/rye pin $(PYTHON_VERSION)
	$(HOME)/.rye/shims/rye add ipython pytest pytest-cov --dev
	$(HOME)/.rye/shims/rye sync --no-lock

test:
	$(HOME)/.rye/shims/rye run pytest

run: 
	$(HOME)/.rye/shims/rye run python main.py

lint:
	$(HOME)/.rye/shims/rye lint -q -- --select I --fix 

format:
	$(HOME)/.rye/shims/rye fmt

all: devinstall lint format test