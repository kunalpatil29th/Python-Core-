# threading_module.py

"""
Definition: The 'threading' module allows you to run multiple operations concurrently in the same process. 
It is useful for I/O-bound tasks.
"""

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Thread 1: {i}")

def print_letters():
    for char in "abcde":
        time.sleep(1)
        print(f"Thread 2: {char}")

# Creating threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Starting threads
print("Starting threads...")
t1.start()
t2.start()

# Waiting for threads to finish
t1.join()
t2.join()
print("All threads finished.")
