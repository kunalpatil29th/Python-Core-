# os_operations.py

"""
Definition: The 'os' module provides a portable way of using operating system dependent functionality 
like file path manipulation, directory creation, and process management.
"""

import os

# Get current working directory
cwd = os.getcwd()
print(f"Current Directory: {cwd}")

# List files in current directory
files = os.listdir(".")
print(f"Files found: {len(files)}")

# Check if a path exists
path = "01_Basics"
print(f"Does '{path}' exist? {os.path.exists(path)}")
