# random_module.py

"""
Definition: The 'random' module implements pseudo-random number generators for various distributions. 
It is widely used for games, simulations, and data shuffling.
"""

import random

# Random float between 0 and 1
print("Random float:", random.random())

# Random integer in range [a, b]
print("Random integer (1-100):", random.randint(1, 100))

# Random choice from a list
choices = ["apple", "banana", "cherry", "date"]
print("Random choice:", random.choice(choices))

# Shuffling a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)
