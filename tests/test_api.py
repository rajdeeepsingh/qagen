import requests


def test_status_code(sample_post):
    assert sample_post.status_code == 200


def test_has_title(sample_post):
    data = sample_post.json()
    assert "title" in data


def test_has_correct_id(sample_post):
    data = sample_post.json()
    assert data["id"] == 1


def test_invalid_post_returns_404(jsonplaceholder_url, request_timeout):
    response = requests.get(
        f"{jsonplaceholder_url}/posts/99999",
        timeout=request_timeout,
    )
    assert response.status_code == 404
