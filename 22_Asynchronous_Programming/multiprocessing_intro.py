# multiprocessing_intro.py

"""
Definition: The 'multiprocessing' module allows the programmer to fully leverage multiple processors on a given machine. It side-steps the Global Interpreter Lock (GIL) by using subprocesses instead of threads.
"""

def simulate_multiprocessing():
    print("Spawning Process 1 (CPU 0)...")
    print("Spawning Process 2 (CPU 1)...")
    print("Heavy computation running in parallel...")
    print("Both processes finished.")

simulate_multiprocessing()
