# decorators.py

"""
Definition: Decorators are a powerful and expressive way to modify the behavior of functions or classes. 
They allow you to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.
"""

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()
