# armstrong_number.py

"""
Problem: Armstrong Number
Check if a number is an Armstrong number (sum of cubes of its digits is equal to the number itself).
"""

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return n == sum(int(digit)**power for digit in num_str)

# Example
num = 153
print(f"Is {num} an Armstrong number? {is_armstrong(num)}")
