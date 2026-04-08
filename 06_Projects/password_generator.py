# password_generator.py

"""
Project: Random Password Generator
Generates a secure random password with mixed characters.
"""

import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("Generated Password:", generate_password(12))
