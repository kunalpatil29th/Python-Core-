# factorial.py

"""
Problem: Factorial Calculation
Find the factorial of a given number using recursion and iteration.
"""

# Recursive approach
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative approach
def factorial_iterative(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

num = 5
print(f"Factorial of {num} (Recursive): {factorial_recursive(num)}")
print(f"Factorial of {num} (Iterative): {factorial_iterative(num)}")
