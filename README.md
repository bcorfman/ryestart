# ultraviolet

My opinionated [Cookiecutter] template for beginning a Python application with Uv dependency management and other modern tooling.

_____
## Features

* [Uv] and pyproject.toml for managing packages and virtualenvs. Uv also [downloads and installs Python versions automatically](https://docs.astral.sh/uv/#python-management) if needed, so you don't have to.
* A Makefile for handling project tasks. (Noah Gift on [Why You Would Want a Makefile in Your Python Project](https://www.youtube.com/watch?v=Kvxaj6pHeVA&t=624s).)
* Batteries included: [ipython] installed as a Uv tool, and [pytest], and [pytest-cov] installed as development dependencies.
* A set of VSCode files (`extensions.json`, `launch.json` and `settings.json`) that will configure debug mode, Pytest execution, auto format/lint on save (via EmeraldWalk's [Run on Save]), plus other Makefile tasks within the sidebar (via Carlos A. Gomes' [Make support and task provider].)
* A GitHub repo will be set up for your project automatically, with the initial code pushed into it. 

______
## Assumptions

* The template requires Mac OS X, Linux, or WSL2 on Windows with a quality Linux distro like Ubuntu. (WSL2/Ubuntu is what I use.)
* [Homebrew must be installed](https://brew.sh).
* Git is linked to an [appropriate credential manager](https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/credstores.md) on your system.
  - On WSL2/Ubuntu, my preference is to use the Windows Credential Manager: `git config --global credential.credentialStore wincredman`
  - On Mac OS X, my preference is to use the default Keychain Access. If you need to set it yourself for some reason, you can do it with `git config --global credential.credentialStore keychain`

_______
## Quickstart

* See Assumptions above.

* [Install Uv](https://docs.astral.sh/uv/getting-started/installation/) then Cookiecutter using `uv tool install cookiecutter`. This makes Cookiecutter available as a [user-wide tool](https://docs.astral.sh/uv/getting-started/features/#tools). This is what I do.

  OR

* Install the latest Cookiecutter [using their instructions](https://cookiecutter.readthedocs.io/en/2.6.0/installation.html). This has the disadvantage of tying the tool to a system-level Python, or you can use something like `pipx` for an isolated install. However, this is yet another Python dependency manager that you will need to keep updated.


Now generate the project:

    cookiecutter gh:bcorfman/ultraviolet

The setup does several things:
  - Prompts for a few needed project configuration details like Project/Repo name, Author name, email and desired Python version that will be installed by Rye.
  - Installs the GitHub CLI and/or Uv via Homebrew, if they aren't installed already.
  - Pulls your GitHub username and PAT from Git Credential Manager and uses them to authenticate to your account.
  - Checks for the existence of the Repo name on your GitHub account; if it's already there, the setup aborts with an error.
  - `git init` is called inside the project directory to create a Git repo.
  - `make devinstall` is executed to install some basic Python dev libraries: `pytest` and `pytest-cov`.
  - Finally, the configured project is committed to the new Git repo and pushed up to your GitHub repo as well. 

Get inside the newly created project:

    cd <repo_name>

_Start working!_

___
## Can you modify how ultraviolet works? Yes!

`ultraviolet` is built the way I like it. But what if it's not configured the way you work?

* One regular annoyance is that Cookiecutter will always prompt you for your name and your email ... Unless you like typing these over and over, the best thing is to create a `.cookiecutterrc` inside your home directory.
  
  For instance, my `~/.cookiecutterrc` looks like this:

  ```
  default_context:
    author_name: "Brandon Corfman"
    author_email: "h9tbgnbbk@privaterelay.appleid.com"
  ```
  
* If you want to install different default libraries inside your project besides the ones I've chosen, modify the `devinstall` section of the [Makefile](https://github.com/bcorfman/ultraviolet/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/Makefile).
* If you want to customize the entire setup process, take a look in [post_gen_project.py](https://github.com/bcorfman/ultraviolet/blob/main/hooks/post_gen_project.py). 
* Finally, since `ultraviolet` has a permissive [license](https://github.com/bcorfman/ultraviolet/blob/main/LICENSE), fork the project and contribute back via a pull request, or turn that fork into [a standalone repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/detaching-a-fork) and make the customizations your own. 

___________________________
## Available Makefile tasks

    make devinstall   # installs all project & development tooling. Executed by Cookiecutter in
                      #   post_gen_project.py hook.
    make install      # installs project files only. No development toolking.
    make run          # prints "Hello World" as a sample
    make test         # tests that "Hello World" is printed
    make lint         # automatically orders imports and fixes code issues with Ruff. 
                      # Linting is customized in pyproject.toml
    make format       # Automatically formats your code and imports with Ruff. 
                      # Formatting is customized in pyproject.toml.

______________________
## Directory structure

This is what your new project will look like:

    ├── .gitignore            <- A modest Python .gitignore customized for this project
    ├── LICENSE               <- The project's MIT license with your name.
    ├── README.md             <- The top-level README for developers using this project.
    ├── Makefile              <- Configure/build/formatting/test tasks that can be run from the command-line. 
    ├── main.py               <- The top-level application file.
    ├── pyproject.toml        <- Rye-compatible TOML file reproducing the development environment
    │    
    ├── .vscode               <- Visual Studio Code configuration files
    |   ├── extensions.json   <- VSCode extension recommendations that will make your development easier.
    |   ├── launch.json       <- Configures VSCode to run and debug the project.
    |   └── settings.json     <- Calls RunOnSave extension to format and lint the code whenever the project is saved.
    |
    ├── src/[module_name]     <- Core Python source files
    |   ├── __init__.py       <- Makes the core directory a module that can be imported
    |   └── example.py        <- A starter submodule that prints "Hello World!"
    |
    └── tests                     
        ├── __init__.py       <- Makes the tests directory a module that can be imported
        └── test_example.py   <- tests that "Hello World!" is printed by the example module



[Cookiecutter]: https://github.com/audreyr/cookiecutter
[Uv]: https://docs.astral.sh/uv/
[ipython]: https://ipython.org
[pytest]: https://docs.pytest.org/en
[Run on Save]: https://marketplace.visualstudio.com/items?itemName=emeraldwalk.RunOnSave
[Make support and task provider]: https://marketplace.visualstudio.com/items?itemName=carlos-algms.make-task-provider
[pytest-cov]: https://pytest-cov.readthedocs.io/en/latest/readme.html
