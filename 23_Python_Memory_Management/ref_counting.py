# ref_counting.py

"""
Definition: Reference Counting is the primary mechanism for memory management in Python 
(specifically CPython). Every object maintains a count of how many references point to it. 
When an object's reference count drops to zero, the memory occupied by that object 
is immediately deallocated. The 'sys.getrefcount()' function can be used 
to check the reference count of an object.
"""

import sys

def check_ref_count():
    print("Creating a list object...")
    a = [1, 2, 3]
    
    # sys.getrefcount() itself adds 1 reference (the argument)
    print(f"Initial reference count of 'a': {sys.getrefcount(a)}") # ~2 (a + argument)
    
    b = a
    print(f"Reference count of 'a' after 'b = a': {sys.getrefcount(a)}") # ~3 (a + b + argument)
    
    c = [a, b]
    print(f"Reference count of 'a' after adding to list 'c': {sys.getrefcount(a)}") # ~5 (a + b + c[0] + c[1] + argument)
    
    # Remove references
    print("\nRemoving references...")
    del b
    print(f"Reference count of 'a' after 'del b': {sys.getrefcount(a)}") # ~4
    
    del c
    print(f"Reference count of 'a' after 'del c': {sys.getrefcount(a)}") # ~2 (back to 'a' + argument)
    
    # Object will be destroyed when 'a' is deleted or goes out of scope
    del a
    # a is no longer accessible here

def main():
    check_ref_count()

if __name__ == "__main__":
    main()
