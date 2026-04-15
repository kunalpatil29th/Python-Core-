# secure_api_keys.py

"""
Definition: API Keys are used to authenticate and authorize access to APIs. They should be stored securely (e.g., environment variables) and never hardcoded.
"""

import os

def get_api_key():
    # Simulated fetching from environment variables
    # In reality, you'd use os.environ.get("API_KEY")
    api_key = os.environ.get("API_KEY", "DEFAULT_MOCK_KEY_12345")
    return api_key

def call_api():
    key = get_api_key()
    print(f"Calling API with key: {key[:5]}*****")

# Usage
call_api()
