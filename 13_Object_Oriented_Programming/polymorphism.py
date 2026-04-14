# polymorphism.py

"""
Definition: Polymorphism means "many forms". It allows us to define methods in the child class with the same name as defined in their parent class.
"""

class Bird:
    def sound(self):
        return "Tweet tweet"

class Duck:
    def sound(self):
        return "Quack quack"

class Cow:
    def sound(self):
        return "Moo moo"

# Polymorphic function
def make_sound(animal_obj):
    print(animal_obj.sound())

# Different objects passed to the same function
make_sound(Bird())
make_sound(Duck())
make_sound(Cow())
