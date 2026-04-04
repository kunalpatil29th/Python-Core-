# functions.py

"""
Definition: A function is a block of reusable code that performs a specific task. 
Functions help in breaking down complex programs into smaller, manageable parts.
"""

# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling a function
message = greet("Kunal")
print(message)

# Function with default arguments
def add(a, b=10):
    return a + b

print("Sum (with default):", add(5))
print("Sum (without default):", add(5, 20))
