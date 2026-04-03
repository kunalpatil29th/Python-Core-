# lists.py

"""
Definition: A list is an ordered, mutable collection of items. 
Lists are written with square brackets [] and can contain different data types.
"""

# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing items
print("First fruit:", fruits[0])

# Modifying items
fruits[1] = "blueberry"
print("Updated list:", fruits)

# Adding items
fruits.append("date")
print("Appended list:", fruits)

# Removing items
fruits.remove("apple")
print("Final list:", fruits)
