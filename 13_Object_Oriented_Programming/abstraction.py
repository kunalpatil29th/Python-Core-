# abstraction.py

"""
Definition: Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object. In Python, this is often done using abstract base classes (abc).
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# shape = Shape() # This would raise a TypeError because Shape is abstract
rect = Rectangle(10, 5)
print(f"Area of the rectangle: {rect.area()}")
