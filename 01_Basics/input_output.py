# input_output.py 

"""
Definition: 
Input: The process of receiving data from the user or an external source (using the input() function).
Output: The process of displaying data to the console or an external destination (using the print() function).
"""

name = input("Enter your name: ") 
age = int(input("Enter your age: ")) 

print("Hello", name) 
print("You are", age, "years old") 

# Using f-strings (formatted string literals)
print(f"Welcome {name}, you will be {age + 1} next year!")
