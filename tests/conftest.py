import pytest
from dotenv import dotenv_values

from clients.api_client import APIClient

BASE_URL = dotenv_values(".env")["BASE_URL"]

@pytest.fixture(scope="session")
def api_client():
    return APIClient(BASE_URL)
