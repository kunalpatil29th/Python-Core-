# file_handling.py

"""
Definition: File handling in Python involves opening, reading, writing, and closing files. 
It allows programs to persist data even after they finish executing.
"""

# Writing to a file
with open("test.txt", "w") as f:
    f.write("Hello, this is a test file.\n")
    f.write("Python file handling is easy!")

# Reading from a file
with open("test.txt", "r") as f:
    content = f.read()
    print("File Content:\n", content)

# Note: The 'with' keyword ensures that the file is automatically closed.
