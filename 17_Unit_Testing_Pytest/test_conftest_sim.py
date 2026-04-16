# test_conftest_sim.py

"""
Definition: 'conftest.py' is a special file in Pytest used to share fixtures and configuration across multiple test files in a directory.
"""

def simulate_conftest_usage():
    print("Simulating shared fixtures from conftest.py...")
    print("Fixture: db_connection -> SUCCESS")
    print("Fixture: app_config -> LOADED")

simulate_conftest_usage()
