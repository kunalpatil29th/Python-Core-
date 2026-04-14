# magic_dunder_methods.py

"""
Definition: Magic (or Dunder) methods in Python are special methods that start and end with double underscores (e.g., __init__, __str__). They allow you to define how objects of your class behave with built-in Python operations.
"""

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Defines how the object is printed as a string
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # Defines behavior for the built-in len() function
    def __len__(self):
        return self.pages

my_book = Book("Python Crash Course", "Eric Matthes", 544)

print(my_book)            # Uses __str__
print(len(my_book))       # Uses __len__
