# test_assertions.py

"""
Definition: Assertions are statements that check if a condition is true. If the condition is false, the test fails.
"""

def test_complex_assertions():
    l1 = [1, 2, 3]
    l2 = [1, 2, 3]
    assert l1 == l2
    assert 1 in l1
    assert "apple" not in l1
    assert isinstance(l1, list)
    print("Assertion tests passed!")
