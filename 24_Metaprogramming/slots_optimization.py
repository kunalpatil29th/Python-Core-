# slots_optimization.py

"""
Definition: The '__slots__' attribute is a memory optimization technique in Python. 
By default, Python uses a dictionary ('__dict__') to store instance attributes, 
which consumes significant memory. When '__slots__' is defined in a class, 
Python reserves a fixed amount of space for the specified attributes and 
prevents the creation of '__dict__', leading to faster attribute access 
and reduced memory overhead.
"""

import sys

class StandardPoint:
    """A standard class using __dict__ for attributes."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedPoint:
    """A class using __slots__ to optimize memory."""
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    print("--- Slots Optimization Demo ---")
    
    p1 = StandardPoint(10, 20)
    p2 = SlottedPoint(10, 20)

    print(f"StandardPoint instance has __dict__? {hasattr(p1, '__dict__')}")
    print(f"SlottedPoint instance has __dict__? {hasattr(p2, '__dict__')}")

    # Comparing memory footprint
    # sys.getsizeof() doesn't include the size of the dictionary for standard objects
    # so we need to add the size of __dict__ explicitly for an accurate comparison.
    std_size = sys.getsizeof(p1) + sys.getsizeof(p1.__dict__)
    slot_size = sys.getsizeof(p2)

    print(f"\nApproximate memory size of StandardPoint: {std_size} bytes")
    print(f"Approximate memory size of SlottedPoint: {slot_size} bytes")
    print(f"Memory saved: {std_size - slot_size} bytes (per instance)")

    # Attempting to add a new attribute
    print("\nAttempting to add 'z' to StandardPoint...")
    p1.z = 30
    print(f"p1.z: {p1.z}")

    print("\nAttempting to add 'z' to SlottedPoint...")
    try:
        p2.z = 30
    except AttributeError as e:
        print(f"Caught expected error: {e}")
        print("Slotted classes prevent adding attributes not defined in __slots__.")

if __name__ == "__main__":
    main()
