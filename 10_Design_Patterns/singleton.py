# singleton.py

"""
Definition: The Singleton Pattern ensures that a class has only one instance and provides a global point of access to it.
"""

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()

print(f"Is s1 same as s2? {s1 is s2}")
