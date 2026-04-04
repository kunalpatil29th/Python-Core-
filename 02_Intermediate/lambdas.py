# lambdas.py

"""
Definition: A lambda function is a small, anonymous function defined with the 'lambda' keyword. 
They can have any number of arguments but only one expression.
"""

# Lambda function for addition
add = lambda x, y: x + y
print("Sum using lambda:", add(10, 20))

# Lambda function for squaring
square = lambda x: x ** 2
print("Square using lambda:", square(5))

# Using lambda with filter()
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)
