# dynamic_attribute_access.py

"""
Definition: Dynamic Attribute Access is the ability of an object to customize 
how its attributes are handled at runtime using special methods like 
'__getattr__()', '__setattr__()', '__getattribute__()', and '__dir__()'. 
This is useful for creating flexible objects like proxies, wrappers, 
or objects that fetch data from an external source on demand.
"""

class FlexibleObject:
    """A class that can store arbitrary attributes dynamically."""
    def __init__(self, **kwargs):
        # We use super().__setattr__ to avoid recursion if we override __setattr__
        for key, value in kwargs.items():
            super().__setattr__(key, value)
        self._data = {}

    def __getattr__(self, name):
        # Called ONLY if the attribute is NOT found through normal means
        print(f"Attribute '{name}' not found. Searching in _data...")
        if name in self._data:
            return self._data[name]
        return f"Attribute '{name}' is undefined."

    def __setattr__(self, name, value):
        # Called for EVERY attribute assignment
        print(f"Setting attribute '{name}' to {value}...")
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            self._data[name] = value

    def __delattr__(self, name):
        # Called for attribute deletion
        print(f"Deleting attribute '{name}'...")
        if name in self._data:
            del self._data[name]
        else:
            super().__delattr__(name)

    def __dir__(self):
        # Called when dir() is invoked on the object
        return sorted(list(self.__dict__.keys()) + list(self._data.keys()))

def main():
    print("--- Dynamic Attribute Access Demo ---")
    obj = FlexibleObject(fixed_attr="Fixed Value")
    
    # Standard attribute access
    print(f"Fixed Attribute: {obj.fixed_attr}")

    # Dynamic attribute assignment
    print("\nAssigning dynamic attribute 'age'...")
    obj.age = 25
    print(f"Age: {obj.age}")

    # Accessing undefined attribute
    print("\nAccessing undefined attribute 'location'...")
    print(obj.location)

    # Listing attributes with dir()
    print("\nAttributes found with dir():")
    print(dir(obj))

    # Deleting dynamic attribute
    print("\nDeleting 'age'...")
    del obj.age
    print(f"Age after deletion: {obj.age}")

if __name__ == "__main__":
    main()
