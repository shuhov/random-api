import pytest

from random_api.app import app


@pytest.fixture
def client():
    return app.test_client()
