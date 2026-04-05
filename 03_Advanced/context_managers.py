# context_managers.py

"""
Definition: Context managers allow you to allocate and release resources precisely when you want to. 
The most common example is the 'with' statement, used for file handling or database connections.
"""

class SimpleContextManager:
    def __enter__(self):
        print("Entering the context...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context...")

# Using the custom context manager
with SimpleContextManager():
    print("Inside the context block.")
