# locks_and_semaphores.py

"""
Definition: Synchronization primitives like Locks and Semaphores are used in asyncio 
to manage access to shared resources and prevent race conditions. 
A Lock ensures only one coroutine can access a critical section at a time, 
while a Semaphore limits access to a fixed number of concurrent coroutines.
"""

import asyncio

# Shared resource
shared_counter = 0

async def worker_with_lock(lock, worker_id):
    """Uses a lock to increment a shared counter safely."""
    global shared_counter
    async with lock:
        print(f"Worker {worker_id} acquired the lock.")
        current_val = shared_counter
        await asyncio.sleep(0.1) # Simulate some work
        shared_counter = current_val + 1
        print(f"Worker {worker_id} released the lock. Counter: {shared_counter}")

async def worker_with_semaphore(semaphore, worker_id):
    """Uses a semaphore to limit the number of concurrent tasks."""
    async with semaphore:
        print(f"Worker {worker_id} entered the critical section.")
        await asyncio.sleep(0.5) # Simulate some work
        print(f"Worker {worker_id} leaving.")

async def main():
    # Example 1: Using a Lock
    lock = asyncio.Lock()
    print("--- Using Lock ---")
    await asyncio.gather(*(worker_with_lock(lock, i) for i in range(5)))
    print(f"Final shared_counter: {shared_counter}\n")

    # Example 2: Using a Semaphore
    # Limit to only 2 concurrent workers
    semaphore = asyncio.Semaphore(2)
    print("--- Using Semaphore (limit 2) ---")
    await asyncio.gather(*(worker_with_semaphore(semaphore, i) for i in range(5)))

if __name__ == "__main__":
    asyncio.run(main())
