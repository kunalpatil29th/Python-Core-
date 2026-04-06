# collections_module.py

"""
Definition: The 'collections' module implements specialized container datatypes providing alternatives to Python’s general purpose built-in containers (dict, list, set, tuple).
"""

from collections import Counter, namedtuple, defaultdict

# Counter: counts hashable objects
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print("Word counts:", count)

# namedtuple: tuple subclasses with named fields
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(f"Point: x={p.x}, y={p.y}")

# defaultdict: dict subclass that calls a factory function to supply missing values
d = defaultdict(int)
d["a"] += 1
print("Defaultdict value:", d["a"])
print("Defaultdict missing key:", d["b"])
