# prime_number.py

"""
Problem: Prime Number Check
Determine if a given number is a prime number (only divisible by 1 and itself).
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example
num = 17
print(f"Is {num} a prime number? {is_prime(num)}")
