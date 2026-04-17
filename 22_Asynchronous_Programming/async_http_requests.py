# async_http_requests.py

"""
Definition: Libraries like 'aiohttp' allow making asynchronous HTTP requests, enabling a single thread to handle thousands of concurrent requests.
"""

def simulate_async_http():
    print("Requesting 10 URLs concurrently...")
    print("  - URL 1: 200 OK")
    print("  - URL 2: 200 OK")
    print("  ... all requests finished in 0.5s")

simulate_async_http()
