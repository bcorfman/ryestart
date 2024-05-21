# pystart

My opinionated [Cookiecutter] template for beginning a Python application with modern tooling.

To be clear, this template is **not** for Python libraries. 

## Features

* [Rye] for managing packages and virtualenvs.
* A Makefile for handling project tasks. 
* Batteries included: [ipython], [pytest], and [pytest-cov] installed as development dependencies.
* A set of VSCode files (`extensions.json`, `launch.json` and `settings.json`) that will configure debug mode, Pytest execution, auto format/lint on save, plus other Makefile tasks within the sidebar.
* A GitHub repo will be set up for your project automatically, with the initial code pushed into it. 

## Assumptions

* The template requires Mac OS X, Linux, or WSL2 on Windows with a quality Linux distro like Ubuntu. (WSL2/Ubuntu is what I use.)
* [Homebrew must be installed](https://brew.sh).

## Quickstart

* See Assumptions above.

* [Install Rye](https://rye-up.com) then Cookiecutter using `rye tools install cookiecutter`. This makes Cookiecutter available as a [global tool](https://rye-up.com/guide/tools/). This is what I do.

OR

* Install the latest Cookiecutter [using their instructions](https://cookiecutter.readthedocs.io/en/2.6.0/installation.html). This has the disadvantage of tying the tool to a system-level Python, or you can use something like `pipx` for an isolated install. However, this is yet another Python dependency manager that you will need to manage.


Now generate the project:

    cookiecutter gh:bcorfman/pystart

The setup does several things:
  - Prompts for a few needed project configuration details like Project/Repo name, Author name, email and desired Python information.
  - Installs the GitHub CLI and Rye using Homebrew, if they aren't installed already.
  - Pulls your GitHub username and PAT from Git Credential Manager and uses them to authenticate to your account.
  - Checks for the existence of the Repo name on your GitHub account; if it's already there, the setup aborts with an error.
  - 'git init` is called inside the project directory to create a Git repo.
  - `make devinstall` is executed to install some basic Python dev libraries: `ipython`, `pytest` and `pytest-cov`.
  - Finally, the configured project is committed to the new Git repo and pushed up to your GitHub repo as well. 

Get inside the newly created project:

    cd <repo_name>

Start working!

## Available Makefile tasks

    make devinstall   # installs all project & development tooling. Executed by Cookiecutter in post_gen_project hook.
    make install      # installs project files only. No development toolking.
    make run          # prints "Hello World" as a sample
    make test         # tests that "Hello World" is printed
    make lint         # automatically orders imports and fixes code issues with Ruff. Customize in pyproject.toml.
    make format       # automatically formats your code with Ruff. Customize in pyproject.toml.

## Directory structure

This is what your new project will look like:

    ├── .gitignore                <- A modest Python .gitignore customized for this project
    ├── LICENSE                   <- The project's MIT license with your name.
    ├── README.md                 <- The top-level README for developers using this project.
    ├── Makefile                  <- Configure/build/formatting/test tasks that can be run from the command-line. 
    ├── main.py                   <- The top-level application file.
    ├── pyproject.toml            <- Rye-compatible TOML file reproducing the development environment
    │    
    ├── .vscode                   <- Visual Studio Code configuration files
    |   ├── extensions.json       <- VSCode extension recommendations that will make your development easier.
    |   ├── launch.json           <- Configures VSCode to run and debug the project.
    |   └── settings.json         <- Calls RunOnSave extension to format and lint the code whenever the project is saved.
    |
    ├── core                      <- Core Python source files
    |   ├── __init__.py           <- Makes the core directory a module that can be imported
    |   └── hello.py              <- A starter submodule that prints "Hello World!"
    |
    └── tests                     
        ├── __init__.py           <- Makes the tests directory a module that can be imported
        └── test_hello.py         <- tests that "Hello World!" is printed by the core.hello module



[Cookiecutter]: https://github.com/audreyr/cookiecutter
[Rye]: https://rye-up.com
[ipython]: https://ipython.org
[pytest]: https://docs.pytest.org/en
[pytest-cov]: https://pytest-cov.readthedocs.io/en/latest/readme.html
