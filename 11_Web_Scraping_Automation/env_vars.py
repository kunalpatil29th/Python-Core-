# env_vars.py

"""
Definition: Environment variables are dynamic-named values that can affect the way running processes 
will behave on a computer. In Python, they are accessed via 'os.environ'.
"""

import os

# Setting an environment variable (session-based)
os.environ["APP_MODE"] = "Development"

# Getting an environment variable
mode = os.environ.get("APP_MODE", "Not Set")
print(f"Application Mode: {mode}")

# Getting system path (partial)
print(f"System Path starts with: {os.environ.get('PATH', '')[:50]}...")
