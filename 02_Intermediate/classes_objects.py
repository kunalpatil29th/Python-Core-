# classes_objects.py

"""
Definition: Object-Oriented Programming (OOP) is a paradigm based on the concept of "objects," 
which can contain data (attributes) and code (methods). A 'class' is a blueprint for objects.
"""

//# Defining a class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating objects (instances of a class)
s1 = Student("Kunal", 20)
s2 = Student("Rahul", 22)

# Accessing attributes and methods
s1.display_info()
s2.display_info()
