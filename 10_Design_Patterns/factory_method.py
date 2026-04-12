# factory_method.py

"""
Definition: The Factory Method Pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate.
"""

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def get_pet(pet_type):
    pets = {"dog": Dog(), "cat": Cat()}
    return pets.get(pet_type, "Unknown pet")

# Usage
print(f"Dog says: {get_pet('dog').speak()}")
print(f"Cat says: {get_pet('cat').speak()}")
