# test_mocking.py

"""
Definition: Mocking is a technique where you replace parts of your system under test with "mock" objects to isolate the code being tested.
"""

from unittest.mock import MagicMock

def fetch_from_api():
    # Imagine this calls a real web API
    return "Real Data"

def test_api_call():
    # Mock the function
    fetch_from_api = MagicMock(return_value="Mocked Data")
    result = fetch_from_api()
    assert result == "Mocked Data"
    print("Mocking test passed!")
