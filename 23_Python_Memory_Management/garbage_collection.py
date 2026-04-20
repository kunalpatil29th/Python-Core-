# garbage_collection.py

"""
Definition: Garbage collection (GC) in Python is an automatic memory management process 
that frees up memory by removing objects that are no longer in use. 
Python's GC uses a combination of Reference Counting and a cyclic garbage collector 
that detects and cleans up objects with circular references using generations (0, 1, 2).
"""

import gc
import sys

class MyObject:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print(f"Object {self.name} is being destroyed by GC.")

def test_circular_reference():
    """Demonstrates circular reference that GC needs to handle."""
    print("Creating circular reference...")
    obj1 = MyObject("A")
    obj2 = MyObject("B")
    
    # Circular link
    obj1.link = obj2
    obj2.link = obj1
    
    # Remove references from local scope
    obj1 = None
    obj2 = None
    print("Local references removed. Circular reference still exists in memory.")

def main():
    # Show GC status
    print(f"Is GC enabled? {gc.isenabled()}")
    print(f"GC Thresholds: {gc.get_threshold()}")

    test_circular_reference()

    # Manually trigger garbage collection
    print("Manually triggering GC...")
    collected = gc.collect()
    print(f"GC collected {collected} objects.")

    # Another example: large list
    print("\nCreating a large list...")
    large_list = [i for i in range(1000000)]
    del large_list
    print("Large list deleted. GC will handle it eventually or on manual trigger.")
    gc.collect()

if __name__ == "__main__":
    main()
