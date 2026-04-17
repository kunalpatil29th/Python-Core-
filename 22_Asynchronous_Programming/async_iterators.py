# async_iterators.py

"""
Definition: An asynchronous iterator is an object that implements the '__aiter__' and '__anext__' methods. It allows for iterating over data that is fetched asynchronously.
"""

def simulate_async_iterator():
    items = ["Data_1", "Data_2", "Data_3"]
    print("Starting Async Iteration...")
    for item in items:
        print(f"  Fetched asynchronously: {item}")
    print("Async Iteration complete.")

simulate_async_iterator()
