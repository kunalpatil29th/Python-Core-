# comments.py

"""
Definition: Comments are non-executable lines of code used to explain what the code does, 
making it easier for developers to read and understand.
"""

# Single line comment 

""" 
Multi-line comment 
This is used for explanation 
""" 

print("Hello World") 

def add(a, b):
    """
    This is a docstring.
    It explains that this function adds two numbers.
    """
    return a + b

print("Sum:", add(5, 10))
