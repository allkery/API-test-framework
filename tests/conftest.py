import pytest
from clients.api_client import APIClient



@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture
def payload():
    return {
        "title": "My post",
        "body": "Post text",
        "userId": 1
    }