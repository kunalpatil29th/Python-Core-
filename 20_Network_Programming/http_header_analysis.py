# http_header_analysis.py

"""
Definition: HTTP headers allow the client and the server to pass additional information with an HTTP request or response.
"""

def analyze_headers():
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Python/3.12",
        "Authorization": "Bearer token123"
    }
    print("Analyzing HTTP Headers:")
    for key, value in headers.items():
        print(f"  {key}: {value}")

analyze_headers()
