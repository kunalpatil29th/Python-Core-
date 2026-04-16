# test_basic.py

"""
Definition: Basic testing involves checking if individual units of source code work as expected. 
Pytest is a popular testing framework that makes it easy to write simple and scalable test cases.
"""

def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    print("Basic test passed!")

if __name__ == "__main__":
    test_add()
