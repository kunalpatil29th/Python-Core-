# palindrome_check.py

"""
Problem: Palindrome Check
Check if a given string or number is the same when read forwards and backwards.
"""

def is_palindrome(s):
    s = str(s).lower().replace(" ", "")
    return s == s[::-1]

# Examples
test_str = "Radar"
test_num = 121

print(f"Is '{test_str}' a palindrome? {is_palindrome(test_str)}")
print(f"Is {test_num} a palindrome? {is_palindrome(test_num)}")
