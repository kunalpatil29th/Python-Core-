# calculator.py

"""
Project: Simple Calculator
A basic arithmetic calculator that performs addition, subtraction, multiplication, and division.
"""

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): 
    if y == 0: return "Error! Division by zero."
    return x / y

print("Simple Calculator")
print("1.Add 2.Subtract 3.Multiply 4.Divide")

choice = "1" # Simulated choice
num1 = 10
num2 = 5

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
