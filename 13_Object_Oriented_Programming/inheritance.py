# inheritance.py

"""
Definition: Inheritance allows us to define a class that inherits all the methods and properties from another class.
"""

# Base (Parent) Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Derived (Child) Class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

# Using inherited methods
my_dog = Dog("Buddy")
my_dog.eat()  # Inherited from Animal
my_dog.bark() # Specific to Dog
