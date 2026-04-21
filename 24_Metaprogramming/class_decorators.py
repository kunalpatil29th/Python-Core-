# class_decorators.py

"""
Definition: A class decorator is a function that takes a class as an argument and returns 
a new class or the modified version of the original class. Just like function decorators, 
class decorators are used to augment or modify the behavior of classes without 
directly changing their source code. They are applied using the '@decorator' syntax 
above the class definition.
"""

import functools
import time

def singleton(cls):
    """A class decorator that turns a class into a Singleton."""
    instances = {}

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return wrapper

def time_all_methods(cls):
    """A class decorator that adds a timer to all callable methods in a class."""
    for attr_name, attr_value in cls.__dict__.items():
        if callable(attr_value) and not attr_name.startswith('__'):
            def make_timed_method(method):
                @functools.wraps(method)
                def timed_method(*args, **kwargs):
                    start = time.time()
                    result = method(*args, **kwargs)
                    end = time.time()
                    print(f"Method '{method.__name__}' took {end - start:.4f}s to execute.")
                    return result
                return timed_method
            
            setattr(cls, attr_name, make_timed_method(attr_value))
    return cls

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Initializing Database Connection...")

@time_all_methods
class heavy_processor:
    def process_data(self):
        print("Processing heavy data...")
        time.sleep(0.5)
        return "Done"

def main():
    print("--- Singleton Class Decorator ---")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"db1 is db2? {db1 is db2}")

    print("\n--- Method Timer Class Decorator ---")
    processor = heavy_processor()
    processor.process_data()

if __name__ == "__main__":
    main()
