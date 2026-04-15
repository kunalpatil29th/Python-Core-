# encryption_decryption.py

"""
Definition: Encryption is the process of encoding information so that only authorized parties can access it. Decryption is the reverse process.
"""

def simple_xor_cipher(data, key):
    return "".join(chr(ord(c) ^ key) for c in data)

# Usage
secret_data = "SensitiveInformation"
key = 42

encrypted = simple_xor_cipher(secret_data, key)
print(f"Encrypted: {encrypted}")

decrypted = simple_xor_cipher(encrypted, key)
print(f"Decrypted: {decrypted}")
