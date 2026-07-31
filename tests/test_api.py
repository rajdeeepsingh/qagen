import requests

REQUEST_TIMEOUT = 10


def test_status_code(sample_post):
    assert sample_post.status_code == 200


def test_has_title(sample_post):
    data = sample_post.json()
    assert "title" in data


def test_has_correct_id(sample_post):
    data = sample_post.json()
    assert data["id"] == 1


def test_invalid_post_returns_404(base_url):
    response = requests.get(f"{base_url}/posts/99999", timeout=REQUEST_TIMEOUT)
    assert response.status_code == 404
