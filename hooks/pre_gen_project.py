import re
import sys

REPO_REGEX = r'^[-_a-zA-Z0-9][-_a-zA-Z0-9]+$'
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'


repo_name = '{{ cookiecutter.repo_name }}'
if not re.match(REPO_REGEX, repo_name):
    print('ERROR: The repo name (%s) is not valid. '
          'Use only alphanumeric characters, underscores and dashes.' % repo_name)
    #Exit to cancel project
    sys.exit(1)


module_name = '{{ cookiecutter.source_directory }}'
if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The module name (%s) is not valid. '
          'Please do not use a - and use _ instead' % module_name)
    #Exit to cancel project
    sys.exit(1)