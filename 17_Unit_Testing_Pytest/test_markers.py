# test_markers.py

"""
Definition: Markers in Pytest are used to categorize tests (e.g., slow, fast, web) or apply special behavior (e.g., skip, xfail).
"""

def test_fast():
    assert True

def test_slow_simulated():
    # In pytest, you'd use @pytest.mark.slow
    print("Skipping slow test in simulation...")
    pass

def test_skip_example():
    # In pytest, you'd use @pytest.mark.skip
    print("Test marked as skip.")
