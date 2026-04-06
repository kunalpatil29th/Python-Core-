# itertools_module.py

"""
Definition: The 'itertools' module provides a set of fast, memory-efficient tools for working with iterators. 
It’s highly useful for building complex iterations in a concise way.
"""

import itertools

# count(start, step): Infinite iterator
print("First 5 counts:")
for i in itertools.islice(itertools.count(10, 2), 5):
    print(i, end=" ")
print("\n")

# cycle(iterable): Repeats an iterable infinitely
colors = ["red", "green", "blue"]
cycle_iter = itertools.cycle(colors)
print("Cycling through colors:")
for _ in range(6):
    print(next(cycle_iter), end=" ")
print("\n")

# chain(*iterables): Combines multiple iterables into one
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list(itertools.chain(list1, list2))
print("Chained list:", combined)
