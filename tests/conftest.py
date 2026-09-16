import os

import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

JSONPLACEHOLDER_URL = os.getenv("JSONPLACEHOLDER_URL")
REQRES_URL = os.getenv("REQRES_URL")
REQUEST_TIMEOUT = 10


def _require_url(name: str, value: str | None) -> str:
    if not value:
        pytest.fail(
            f"{name} is not set. Copy .env.example to .env and set {name}."
        )
    return value.rstrip("/")


@pytest.fixture
def request_timeout():
    return REQUEST_TIMEOUT


@pytest.fixture
def jsonplaceholder_url():
    return _require_url("JSONPLACEHOLDER_URL", JSONPLACEHOLDER_URL)


@pytest.fixture
def reqres_url():
    return _require_url("REQRES_URL", REQRES_URL)


@pytest.fixture
def sample_post(jsonplaceholder_url, request_timeout):
    response = requests.get(
        f"{jsonplaceholder_url}/posts/1",
        timeout=request_timeout,
    )
    response.raise_for_status()
    return response
