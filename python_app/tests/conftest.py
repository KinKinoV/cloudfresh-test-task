import os
import tempfile

import pytest
from flaskExample import create_app

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'SECRET_KEY': 'testingkey'
    })

    yield app

@pytest.fixture
def client(app):
    return app.test_client()