# basic_requests.py

"""
Definition: The 'requests' library is used for making HTTP requests in Python. 
It simplifies interacting with web services and APIs.
"""

# Note: This is a simulation as requests might not be installed in all environments
def simulate_get_request(url):
    print(f"Simulating GET request to: {url}")
    return {"status_code": 200, "data": "Sample HTML/JSON content"}

url = "https://api.github.com"
response = simulate_get_request(url)
print(f"Response Status: {response['status_code']}")
