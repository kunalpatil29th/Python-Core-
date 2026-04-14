# class_and_static_methods.py

"""
Definition: 
- Class Methods (@classmethod): Bound to the class and not the object. They can modify class state that applies across all instances.
- Static Methods (@staticmethod): Bound to the class and not the object, but they can't modify class state. They are utility functions.
"""

class MathUtils:
    multiplier = 2

    @classmethod
    def change_multiplier(cls, new_mult):
        cls.multiplier = new_mult
        print(f"Multiplier changed to {cls.multiplier}")

    @staticmethod
    def add(x, y):
        return x + y

# Using static method
print(f"Static method add: {MathUtils.add(5, 10)}")

# Using class method
MathUtils.change_multiplier(5)
