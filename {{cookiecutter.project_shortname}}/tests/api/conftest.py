{% include 'misc/header.py' %}
"""Common pytest fixtures and plugins."""

from __future__ import absolute_import, print_function

import pytest
from invenio_app.factory import create_api


@pytest.fixture(scope='module')
def create_app():
    """Create app fixture."""
    return create_api
