# dictionaries.py

"""
Definition: A dictionary is an unordered, mutable collection of key-value pairs. 
Dictionaries are written with curly braces {} and use keys to access values.
"""

# Creating a dictionary
student = {
    "name": "Kunal",
    "age": 20,
    "is_student": True
}

# Accessing values
print("Name:", student["name"])

# Modifying values
student["age"] = 21

# Adding a new key-value pair
student["course"] = "Python"

print("Updated Dictionary:", student)
