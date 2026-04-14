# classes_and_objects.py

"""
Definition: A Class is a blueprint for creating objects. An Object is an instance of a Class.
"""

class Car:
    # Constructor method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_engine(self):
        self.is_running = True
        print(f"The {self.year} {self.make} {self.model}'s engine is now running.")

# Creating objects (instances)
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

# Accessing attributes and methods
print(f"Car 1: {car1.make} {car1.model}")
car1.start_engine()
