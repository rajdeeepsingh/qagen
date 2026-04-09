import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post_status_code():
    """API 200 return kare"""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_get_post_has_title():
    """Response mein title field ho"""
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "title" in data

def test_get_post_has_correct_id():
    """ID 1 honi chahiye"""
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert data["id"] == 1

def test_invalid_post_returns_404():
    """Fake ID pe 404 aana chahiye"""
    response = requests.get(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404