import os
import pytest

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


def test_temp_path(temp_path: str):
    """Check that temporal path is a valid path."""
    assert temp_path.startswith('/tmp')
    assert not os.path.exists(temp_path)


def test_temp_workspace(temp_workspace: str):
    """Check that temporal workspace folder is a valid path."""
    assert temp_workspace.startswith('/tmp')
    assert os.path.isdir(temp_workspace)
