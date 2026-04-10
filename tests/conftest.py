import pytest
import requests
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def sample_post(base_url):
    response = requests.get(f"{base_url}/posts/1")
    return response