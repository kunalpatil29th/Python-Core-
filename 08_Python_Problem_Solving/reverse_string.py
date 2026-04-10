# reverse_string.py

"""
Problem: Reverse a String
Different ways to reverse a string in Python.
"""

def reverse_slicing(s):
    return s[::-1]

def reverse_iterative(s):
    res = ""
    for char in s:
        res = char + res
    return res

# Example
text = "Python Core"
print(f"Original: {text}")
print(f"Reversed (Slicing): {reverse_slicing(text)}")
print(f"Reversed (Iterative): {reverse_iterative(text)}")
