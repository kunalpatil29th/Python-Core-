# multiple_inheritance.py

"""
Definition: Multiple inheritance allows a class to inherit attributes and methods from more than one parent class.
"""

class Flyer:
    def fly(self):
        print("Flying high in the sky!")

class Swimmer:
    def swim(self):
        print("Swimming deep in the water!")

# Inheriting from both Flyer and Swimmer
class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

donald = Duck()
donald.fly()
donald.swim()
donald.quack()
