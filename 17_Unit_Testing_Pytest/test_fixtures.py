# test_fixtures.py

"""
Definition: Fixtures are functions that run before (and sometimes after) each test function to provide a fixed baseline for tests, such as database connections or test data.
"""

import pytest

def get_data():
    return {"id": 1, "name": "Kunal"}

def test_data_consistency():
    data = get_data()
    assert data["name"] == "Kunal"
    print("Fixture-style test passed!")

# Simulation of @pytest.fixture
def sample_fixture():
    return [1, 2, 3]

def test_with_fixture():
    data = sample_fixture()
    assert len(data) == 3
