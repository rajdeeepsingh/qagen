import requests


def test_get_users_status_code(reqres_url, request_timeout):
    """Users list 200 return kare"""
    response = requests.get(
        f"{reqres_url}/users?page=1",
        timeout=request_timeout,
    )
    assert response.status_code == 200


def test_get_users_has_data(reqres_url, request_timeout):
    """Response mein data field ho"""
    response = requests.get(
        f"{reqres_url}/users?page=1",
        timeout=request_timeout,
    )
    body = response.json()
    assert "data" in body


def test_get_single_user(reqres_url, request_timeout):
    """Single user fetch ho"""
    response = requests.get(
        f"{reqres_url}/users/1",
        timeout=request_timeout,
    )
    body = response.json()
    assert body["data"]["id"] == 1


def test_get_invalid_user_returns_404(reqres_url, request_timeout):
    """Invalid user pe 404 aaye"""
    response = requests.get(
        f"{reqres_url}/users/9999",
        timeout=request_timeout,
    )
    assert response.status_code == 404


def test_login_success(reqres_url, request_timeout):
    """Valid credentials pe token mile"""
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka",
    }
    response = requests.post(
        f"{reqres_url}/login",
        json=payload,
        timeout=request_timeout,
    )
    body = response.json()
    assert response.status_code == 200
    assert "token" in body


def test_login_missing_password(reqres_url, request_timeout):
    """Password missing ho toh 400 aaye"""
    payload = {
        "email": "eve.holt@reqres.in",
    }
    response = requests.post(
        f"{reqres_url}/login",
        json=payload,
        timeout=request_timeout,
    )
    assert response.status_code == 400


def test_register_success(reqres_url, request_timeout):
    """Valid registration pe id aur token mile"""
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol",
    }
    response = requests.post(
        f"{reqres_url}/register",
        json=payload,
        timeout=request_timeout,
    )
    body = response.json()
    assert response.status_code == 200
    assert "token" in body


def test_register_missing_password(reqres_url, request_timeout):
    """Password missing ho toh 400 aaye"""
    payload = {
        "email": "eve.holt@reqres.in",
    }
    response = requests.post(
        f"{reqres_url}/register",
        json=payload,
        timeout=request_timeout,
    )
    assert response.status_code == 400
