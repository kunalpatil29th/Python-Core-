# async_generators.py

"""
Definition: An asynchronous generator is a coroutine that uses 'yield' to produce values one by one while allowing 'await' within its body. 
It is used to iterate over asynchronous data sources, such as reading from a database or a network stream.
Asynchronous generators must be iterated using 'async for'.
"""

import asyncio

async def async_data_generator(limit, delay):
    """Generates values asynchronously after a delay."""
    print(f"Starting async generator (limit: {limit}, delay: {delay}s)...")
    for i in range(1, limit + 1):
        await asyncio.sleep(delay)
        yield f"Data Item {i}"

async def main():
    print("Consuming async generator...")
    # Iterating over the async generator using 'async for'
    async for item in async_data_generator(5, 0.5):
        print(f"Received: {item}")

    print("Finished consuming async generator.")

if __name__ == "__main__":
    asyncio.run(main())
