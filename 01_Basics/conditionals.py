# conditionals.py

"""
Definition: Conditional statements (if, elif, else) are used to perform different 
actions based on different conditions.
"""

age = 18

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# Check even or odd
num = 10
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
