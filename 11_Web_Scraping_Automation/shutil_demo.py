# shutil_demo.py

"""
Definition: The 'shutil' module offers a number of high-level operations on files and collections of files, 
such as copying, moving, and removing.
"""

import shutil
import os

def simulate_shutil():
    source = "temp_src.txt"
    dest = "temp_dest.txt"
    
    # Create dummy file
    with open(source, "w") as f: f.write("test")
    
    # Copy file
    shutil.copy(source, dest)
    print(f"Copied {source} to {dest}")
    
    # Cleanup
    os.remove(source)
    os.remove(dest)
    print("Cleanup complete.")

simulate_shutil()
