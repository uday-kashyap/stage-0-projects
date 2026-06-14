import pytest


@pytest.fixture
def sample_account_data():
    return {"github": [{"username": "example_user", "password": "exampleuser"}]}