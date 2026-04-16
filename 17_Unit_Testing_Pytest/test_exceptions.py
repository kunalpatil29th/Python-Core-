# test_exceptions.py

"""
Definition: Exception testing verifies that your code raises the correct errors when it encounters invalid input or unexpected states.
"""

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide_exception():
    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
        print("Exception test passed!")
