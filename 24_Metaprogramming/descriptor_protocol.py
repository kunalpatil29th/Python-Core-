# descriptor_protocol.py

"""
Definition: The Descriptor Protocol is a set of methods—'__get__()', '__set__()', 
and '__delete__()'—that allow an object to customize how its attributes are accessed, 
assigned, or deleted when used as a class attribute of another class. 
Descriptors are the underlying mechanism for properties, class methods, 
and static methods in Python.
"""

class IntegerField:
    """A descriptor that ensures an attribute is an integer within a specific range."""
    def __init__(self, min_val=None, max_val=None):
        self.min_val = min_val
        self.max_val = max_val
        self.name = None # Will be set by __set_name__

    def __set_name__(self, owner, name):
        # Called when the class is created to let the descriptor know its attribute name
        self.name = name

    def __get__(self, instance, owner):
        # Called when the attribute is accessed
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        # Called when the attribute is assigned
        if not isinstance(value, int):
            raise TypeError(f"'{self.name}' must be an integer.")
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"'{self.name}' must be at least {self.min_val}.")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"'{self.name}' must be at most {self.max_val}.")
        
        instance.__dict__[self.name] = value

class UserProfile:
    # Using the descriptor
    age = IntegerField(min_val=18, max_val=120)
    score = IntegerField(min_val=0)

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def main():
    print("--- Descriptor Protocol Demo ---")
    try:
        user = UserProfile("John", 25, 100)
        print(f"User: {user.name}, Age: {user.age}, Score: {user.score}")

        print("\nUpdating age to 30...")
        user.age = 30
        print(f"New Age: {user.age}")

        print("\nAttempting to set invalid age (15)...")
        user.age = 15
    except (TypeError, ValueError) as e:
        print(f"Caught expected error: {e}")

    try:
        print("\nAttempting to set non-integer score ('high')...")
        user.score = "high"
    except TypeError as e:
        print(f"Caught expected error: {e}")

if __name__ == "__main__":
    main()
