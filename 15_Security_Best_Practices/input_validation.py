# input_validation.py

"""
Definition: Input Validation is the process of ensuring that a program operates on clean, correct, and useful data.
"""

import re

def validate_email(email):
    # Basic regex for email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

def validate_age(age):
    try:
        age_int = int(age)
        return 0 <= age_int <= 120
    except ValueError:
        return False

# Usage
print(f"Email 'test@test.com' valid? {validate_email('test@test.com')}")
print(f"Age '25' valid? {validate_age('25')}")
print(f"Age 'abc' valid? {validate_age('abc')}")
