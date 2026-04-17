# concurrent_tasks.py

"""
Definition: Running tasks concurrently in 'asyncio' means starting multiple coroutines and allowing the event loop to manage their execution without waiting for one to finish before starting the next.
"""

def simulate_concurrency():
    print("Starting Task A, Task B, and Task C concurrently...")
    print("Task B finished (it was fastest)")
    print("Task A finished")
    print("Task C finished (it was slowest)")

simulate_concurrency()
