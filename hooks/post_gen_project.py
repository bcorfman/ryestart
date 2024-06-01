#!/usr/bin/env python
"""Script that runs after the project generation phase."""
from pathlib import Path
from subprocess import call, run, CompletedProcess, CalledProcessError

PROJECT_DIRECTORY = Path.cwd()
MODULE_NAME = "{{ cookiecutter.repo_name }}"

brew_working = False
gh_cli_and_rye_installed = False
git_initialized = False
install_complete = False
auth_to_github = False
git_add = False
git_commit = False
git_rename_branch = False
git_create_repo = False


def subproc(args):
    success = False
    proc = CompletedProcess('', 0)
    try:
        retcode = call(args, shell=True)
        if retcode < 0:
            print("Child was terminated by signal", -retcode, file=proc.stderr)
        else:
            if retcode != 0:
                print("Child returned", retcode, file=proc.stderr)
            else:
                success = True
    except OSError as e:
        print("Execution failed:", e, file=proc.stderr)
    
    return success


def subproc_with_output(cmd, **args):
    success = False
    proc = CompletedProcess('', 0)
    try:
        proc = run(cmd, shell=True, text=True, capture_output=True, check=True)
        if proc.returncode < 0:
            print("Child was terminated by signal", -proc.returncode, file=proc.stderr)
        else:
            if proc.returncode != 0:
                print("Child returned", proc.returncode, file=proc.stderr)
            else:
                success = True
    except OSError as e:
        if not args.get('suppress_failure'):
            print("Execution failed:", e, file=proc.stderr)
        else:
            success = True
    except CalledProcessError as e:
        if not args.get('suppress_failure'):
            print("Execution failed:", e, file=proc.stderr)
        else:
            success = True
    return success, proc.stdout


def main():
    # The basics: you'll need Homebrew on your system. 
    # I could do the install here as well, but that seems a bit too invasive;
    # so it's a prerequisite instead. If you'd rather use some other package manager
    # that works on both Mac and Linux, this is the place to make sure it's installed 
    # and working. 
    brew_working, stdout = subproc_with_output("brew --version")
    if not brew_working or "Homebrew " not in stdout:
        print("Could not find Homebrew on your system.")
        return

    # if GitHub CLI and Rye aren't already installed, install them!
    _, stdout = subproc_with_output("brew list")
    output = stdout.split()
    if 'gh' not in output: 
        gh_cli_installed = subproc("brew install gh")
        if not gh_cli_installed:
            print("Could not perform brew install for GitHub CLI.")
            return 
    if 'rye' not in output: 
        rye_installed = subproc("brew install rye")
        if not rye_installed:
            print("Could not perform brew install for Rye.")
            return 
    
    username = None
    pat = None
    get_pat, stdout = subproc_with_output("echo url=https://github.com | git credential fill")
    if not get_pat:
        print("Couldn't obtain GitHub PAT from Git Credential Manager. Have you used it before?")
        return
    else:
        for line in stdout.splitlines():
            if "username=" in line:
                username = line.split("=")[-1].strip()
            if "password=" in line:
                pat = line.split("=")[-1].strip()
                break
    if not pat or not username:
        print("Could not obtain GitHub username and PAT from Git Credential Manager. Have you used it before?")
        return

    # login to GitHub and add/commit/push the newly created repo
    cmd = f"echo {pat} | gh auth login --with-token"
    auth_to_github = subproc(cmd)
    if not auth_to_github:
        print("Could not authenticate to GitHub. Check PAT content.")
        return 

    repo_check_fail, stdout = subproc_with_output(f'git ls-remote -h "https://github.com/{username}/{MODULE_NAME}.git" &> /dev/null',
                                                  suppress_failure=True)
    if not repo_check_fail:
        print(f"Found an existing repo called {MODULE_NAME} in your GitHub account. Please delete before continuing.")
        return

    git_initialized, _ = subproc_with_output("git init")
    if not git_initialized:
        print("Could not perform git init in project directory.")
        return 

    install_complete, _ = subproc_with_output("make devinstall")
    if not install_complete:
        print("Could not make development environmnent for project.")
        return 

    git_add, _ = subproc_with_output("git add .")
    if not git_add:
        print("Could not perform git add on project files.")
        return 
            
    git_commit, _ = subproc_with_output('git commit -m "Initial commit"')
    if not git_commit:
        print("Could not perform initial git commit.")
        return 
            
    git_rename_branch, _ = subproc_with_output("git branch -M main")
    if not git_rename_branch:
        print("Could not rename master branch to main.")
        return 
            
    git_create_repo, _ = subproc_with_output("gh repo create {{ cookiecutter.repo_name }} --public --push --source=.")
    if not git_create_repo:
        print("Could not create repo on GitHub. Check project name.")
        return 

    print("Done!")
    
if __name__ == "__main__":
    main()

