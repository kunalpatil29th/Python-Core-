# object_interning.py

"""
Definition: Object interning is an optimization technique where only one copy 
of an immutable object (such as small integers and certain strings) is kept in memory. 
This saves memory and speeds up equality comparisons by checking 
the memory address (using 'is') instead of comparing values (using '==').
Python automatically interns small integers (from -5 to 256) and strings that look like identifiers.
"""

import sys

def test_integer_interning():
    """Demonstrates interning of small integers."""
    print("--- Integer Interning ---")
    a = 100
    b = 100
    print(f"a = {a}, b = {b}")
    print(f"a is b? {a is b}") # True (interned)

    c = 500
    d = 500
    print(f"c = {c}, d = {d}")
    print(f"c is d? {c is d}") # False (not interned, but some versions may optimize)

def test_string_interning():
    """Demonstrates interning of strings."""
    print("\n--- String Interning ---")
    s1 = "hello"
    s2 = "hello"
    print(f"s1 = '{s1}', s2 = '{s2}'")
    print(f"s1 is s2? {s1 is s2}") # True (interned)

    # Strings with spaces or special characters are usually NOT interned automatically
    s3 = "hello world!"
    s4 = "hello world!"
    print(f"s3 = '{s3}', s4 = '{s4}'")
    print(f"s3 is s4? {s3 is s4}") # False (not interned automatically)

    # Manual interning using sys.intern()
    s5 = sys.intern("hello world!")
    s6 = sys.intern("hello world!")
    print(f"s5 (interned) is s6 (interned)? {s5 is s6}") # True

def main():
    test_integer_interning()
    test_string_interning()

if __name__ == "__main__":
    main()
