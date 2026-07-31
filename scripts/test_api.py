import requests

REQUEST_TIMEOUT = 10


def check_api(url):
    """Hit an API endpoint and print the result."""
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
    except requests.RequestException as exc:
        print(f"URL     : {url}")
        print(f"❌ Request failed: {exc}")
        return

    print(f"URL     : {url}")
    print(f"Status  : {response.status_code}")

    try:
        body = response.json()
    except ValueError:
        body = response.text

    print(f"Response: {body}")

    if response.status_code == 200:
        print("✅ API is working!")
    else:
        print("❌ Something went wrong.")


# Test karo ek free public API se
check_api("https://jsonplaceholder.typicode.com/posts/1")
