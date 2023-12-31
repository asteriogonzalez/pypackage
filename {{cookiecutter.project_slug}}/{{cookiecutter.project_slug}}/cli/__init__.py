"""CLI for '{{ cookiecutter.project_name }}' package.

# Autocompletion

https://click.palletsprojects.com/en/8.1.x/shell-completion/

_{{ cookiecutter.project_slug.upper() }}_COMPLETE=IGNORE_WINGDEBUG=0 bash_source {{ cookiecutter.project_slug }} > ~/.{{cookiecutter.project_slug}}-complete.bash

. ~/.{{cookiecutter.project_slug}}-complete.bash

"""
import sys
import os

{%- if cookiecutter.use_wingide_remote_debug|lower == 'y' %}
if os.environ.get('IGNORE_WINGDEBUG',False):
    try:
        # print(f"Trying to connect to a remote debugger..")
        sys.path.append(os.path.dirname(__file__))
        from . import wingdbstub
    except Exception:
        print("Remote debugging is not found or configured...")
{%- endif %}

# -----------------------------------------------
# import main cli interface (root)
# -----------------------------------------------

from .main import *
from .config import *
from .workspace import *

# -----------------------------------------------
# import other project submodules/subcommands
# -----------------------------------------------

# from .inventory import inventory
# from .plan import plan
# from .real import real
# from .roles import role
# from .run import run
# from .target import target
# from .test import test
# from .users import user
# from .watch import watch

