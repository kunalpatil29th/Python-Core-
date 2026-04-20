# future_objects.py

"""
Definition: A Future is an object that represents an eventual result of an asynchronous operation. 
It is a low-level object used in 'asyncio' to bridge low-level callback-based code with high-level async/await code.
When a Future is created, it is in a 'pending' state. Once the result is set using 'set_result()', it becomes 'finished'.
"""

import asyncio

async def set_future_result(fut, delay):
    """Sets the result of a future after a delay."""
    await asyncio.sleep(delay)
    print(f"Setting result to: 'Success after {delay}s'")
    fut.set_result(f"Result available after {delay}s")

async def main():
    # Get the current event loop
    loop = asyncio.get_running_loop()

    # Create a Future object
    fut = loop.create_future()

    print(f"Future status before: {fut.done()}") # False

    # Schedule the result setter
    asyncio.create_task(set_future_result(fut, 2))

    # Wait for the future to have a result
    print("Waiting for future...")
    result = await fut

    print(f"Future status after: {fut.done()}") # True
    print(f"Retrieved Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
