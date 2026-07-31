import os

import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
REQUEST_TIMEOUT = 10


@pytest.fixture
def base_url():
    if not BASE_URL:
        pytest.fail(
            "BASE_URL is not set. Copy .env.example to .env and set BASE_URL."
        )
    return BASE_URL.rstrip("/")


@pytest.fixture
def sample_post(base_url):
    response = requests.get(f"{base_url}/posts/1", timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response
