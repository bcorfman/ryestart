#!/usr/bin/env python
"""Script that runs after the project generation phase."""
import sys
from subprocess import call
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()

brew_working = False
gh_cli_and_rye_installed = False
git_initialized = False
install_complete = False
auth_to_github = False
git_add = False
git_commit = False
git_rename_branch = False
git_create_repo = False


def subproc(cmd):
    success = False
    try:
        retcode = call(cmd, shell=True)
        if retcode < 0:
            print("Child was terminated by signal", -retcode, file=sys.stderr)
        else:
            if retcode != 0:
                print("Child returned", retcode, file=sys.stderr)
            else:
                success = True
    except OSError as e:
        print("Execution failed:", e, file=sys.stderr)
    
    return success

def main():
    # The basics: you'll need Homebrew on your system. 
    # I could do the install here as well, but that seems a bit too invasive;
    # so it's a prerequisite instead. If you'd rather use some other package manager
    # that works on both Mac and Linux, this is the place to make sure it's installed 
    # and working. 
    brew_working = subproc("brew update")
    if not brew_working:
        print("Could not perform brew update.")
        return
    
    # install GitHub CLI and Rye.
    gh_cli_and_rye_installed = subproc("brew install gh rye")
    if not gh_cli_and_rye_installed:
        print("Could not perform brew install for GitHub CLI and Rye.")
        return 
    
    # rye init does git init for the repo, along with some other config. 
    # (see Rye docs for complete details).
    git_initialized = subproc("git init")
    if not git_initialized:
        print("Could not perform git init in project directory.")
        return 

    install_complete = subproc("make devinstall")
    if not install_complete:
        print("Could not make development environmnent for project.")
        return 

    # login to GitHub and add/commit/push the newly created repo
    auth_to_github = subproc("gh auth login --with-token < pat.txt")
    if not auth_to_github:
        print("Could not authenticate to GitHub. Check content and location of PAT.")
        return 

    git_add = subproc("git add .")
    if not git_add:
        print("Could not perform git add on project files.")
        return 
            
    git_commit = subproc('git commit -m "Initial commit"')
    if not git_commit:
        print("Could not perform initial git commit.")
        return 
            
    git_rename_branch = subproc("git branch -M main")
    if not git_rename_branch:
        print("Could not rename master branch to main.")
        return 
            
    git_create_repo = subproc("gh repo create {{ cookiecutter.repo_name }} --public --push --source=.")
    if not git_create_repo:
        print("Could not create repo on GitHub. Check project name.")
        return 


if __name__ == "__main__":
    main()