# generators.py

"""
Definition: Generators are functions that return an iterable set of items, one at a time, in a special way. 
They use the 'yield' keyword instead of 'return'. Generators are memory-efficient as they generate items on the fly.
"""

def my_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1

# Using the generator
gen = my_generator(5)
print("Generator items:")
for item in gen:
    print(item)
