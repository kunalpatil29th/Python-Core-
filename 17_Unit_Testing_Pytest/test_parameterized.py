# test_parameterized.py

"""
Definition: Parameterization allows running the same test function with different sets of input data, reducing code duplication.
"""

def multiply(a, b):
    return a * b

def test_multiply():
    test_cases = [
        (2, 3, 6),
        (5, 5, 25),
        (0, 10, 0),
        (-1, 5, -5)
    ]
    for a, b, expected in test_cases:
        assert multiply(a, b) == expected
    print("Parameterized tests passed!")
