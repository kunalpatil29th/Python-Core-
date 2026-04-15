# password_hashing.py

"""
Definition: Password Hashing is the process of transforming a password into a fixed-length string of characters, which is then stored instead of the actual password to improve security.
"""

import hashlib
import os

def hash_password(password):
    # Adding salt for better security
    salt = os.urandom(16)
    # Using SHA-256 for hashing
    h = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return salt + h

def verify_password(stored_hash, input_password):
    salt = stored_hash[:16]
    stored_h = stored_hash[16:]
    new_h = hashlib.pbkdf2_hmac('sha256', input_password.encode(), salt, 100000)
    return new_h == stored_h

# Usage
password = "SecretPassword123"
stored = hash_password(password)
print(f"Password verified: {verify_password(stored, 'SecretPassword123')}")
print(f"Wrong password verified: {verify_password(stored, 'WrongPass')}")
