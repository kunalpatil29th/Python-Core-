# list_comprehensions.py

"""
Definition: List comprehensions provide a concise way to create lists. 
They consist of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
"""

# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)
print("Traditional Squares:", squares)

# List comprehension way
squares_comp = [x**2 for x in range(10)]
print("Comprehension Squares:", squares_comp)

# List comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even Squares:", even_squares)
