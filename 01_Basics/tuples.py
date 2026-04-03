# tuples.py

"""
Definition: A tuple is an ordered, immutable collection of items. 
Tuples are written with parentheses () and cannot be changed after creation.
"""

# Creating a tuple
colors = ("red", "green", "blue")

# Accessing items
print("First color:", colors[0])

# Tuples are immutable - this would cause an error:
# colors[0] = "yellow"

# Tuple length
print("Number of colors:", len(colors))
