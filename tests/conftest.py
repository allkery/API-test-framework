import pytest
from dotenv import load_dotenv

from clients.api_client import APIClient


base_url = load_dotenv(".env")["BASE_URL"]

@pytest.fixture(scope="session")
def api_client():
    return APIClient(base_url)