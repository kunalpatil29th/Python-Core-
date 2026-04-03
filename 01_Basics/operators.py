# operators.py 

"""
Definition: Operators are special symbols used to perform operations on variables and values.
Python includes arithmetic, comparison, logical, and assignment operators.
"""

# Arithmetic Operators 
a = 10 
b = 3 

print(a + b)   # 13 
print(a - b)   # 7 
print(a * b)   # 30 
print(a / b)   # 3.33 
print(a % b)   # 1 
print(a ** b)  # 1000 
print(a // b)  # 3 

# Comparison Operators 
print(10 > 5)    # True 
print(10 == 5)   # False 
print(10 != 5)   # True 

# Logical Operators 
x = True 
y = False 

print(x and y)  # False 
print(x or y)   # True 
print(not x)    # False 

# Assignment Operators 
a = 5 
a += 2  # a = a + 2 
print(a)  # 7 

# Identity Operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 is list3)    # True
print(list1 is list2)    # False
print(list1 == list2)   # True

# Membership Operators
print(1 in list1)       # True
print(4 not in list1)   # True


a = property