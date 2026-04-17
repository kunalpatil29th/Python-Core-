# async_context_managers.py

"""
Definition: An asynchronous context manager is a context manager that is able to suspend execution in its enter and exit methods. It uses 'async with'.
"""

def simulate_async_cm():
    print("async with DatabaseConnection() as db:")
    print("  Entering async context...")
    print("  Executing query...")
    print("  Exiting async context...")

simulate_async_cm()
