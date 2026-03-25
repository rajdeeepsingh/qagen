import requests

def check_api(url):
    """Hit an API endpoint and print the result."""
    response = requests.get(url)
    
    print(f"URL     : {url}")
    print(f"Status  : {response.status_code}")
    print(f"Response: {response.json()}")
    
    if response.status_code == 200:
        print("✅ API is working!")
    else:
        print("❌ Something went wrong.")

# Test karo ek free public API se
check_api("https://jsonplaceholder.typicode.com/posts/1")