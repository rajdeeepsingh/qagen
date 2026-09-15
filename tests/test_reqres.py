import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")


def test_get_users_status_code():
    """Users list 200 return kare"""
    response = requests.get(f"{BASE_URL}/users?page=1")
    assert response.status_code == 200


def test_get_users_has_data():
    """Response mein data field ho"""
    response = requests.get(f"{BASE_URL}/users?page=1")
    body = response.json()
    assert "data" in body


def test_get_single_user():
    """Single user fetch ho"""
    response = requests.get(f"{BASE_URL}/users/1")
    body = response.json()
    assert body["data"]["id"] == 1


def test_get_invalid_user_returns_404():
    """Invalid user pe 404 aaye"""
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404


def test_login_success():
    """Valid credentials pe token mile"""
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    body = response.json()
    assert response.status_code == 200
    assert "token" in body


def test_login_missing_password():
    """Password missing ho toh 400 aaye"""
    payload = {
        "email": "eve.holt@reqres.in"
    }
    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 400


def test_register_success():
    """Valid registration pe id aur token mile"""
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(f"{BASE_URL}/register", json=payload)
    body = response.json()
    assert response.status_code == 200
    assert "token" in body


def test_register_missing_password():
    """Password missing ho toh 400 aaye"""
    payload = {
        "email": "eve.holt@reqres.in"
    }
    response = requests.post(f"{BASE_URL}/register", json=payload)
    assert response.status_code == 400