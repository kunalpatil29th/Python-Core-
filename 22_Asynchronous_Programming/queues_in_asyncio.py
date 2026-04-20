# queues_in_asyncio.py

"""
Definition: asyncio.Queue is a FIFO (First-In, First-Out) queue that allows multiple producer and consumer coroutines to coordinate. 
It is designed to be used in asynchronous environments and provides methods like 'put()' and 'get()' that can be awaited.
Queues are useful for decoupling producer-consumer workloads in asynchronous applications.
"""

import asyncio
import random

async def producer(queue, n):
    """Produces n items and puts them into the queue."""
    for i in range(1, n + 1):
        item = f"Task-{i}"
        await asyncio.sleep(random.uniform(0.1, 0.5))
        await queue.put(item)
        print(f"Producer: Added '{item}' to the queue.")
    
    # Indicate production is finished
    await queue.put(None)

async def consumer(queue):
    """Consumes items from the queue until 'None' is received."""
    while True:
        item = await queue.get()
        if item is None:
            print("Consumer: Finished consuming.")
            queue.task_done()
            break
        
        await asyncio.sleep(random.uniform(0.2, 0.8))
        print(f"Consumer: Processed '{item}'.")
        queue.task_done()

async def main():
    queue = asyncio.Queue()

    # Create producer and consumer tasks
    prod_task = asyncio.create_task(producer(queue, 5))
    cons_task = asyncio.create_task(consumer(queue))

    # Wait for the producer to finish
    await prod_task
    # Wait for all items to be processed
    await queue.join()
    # Cancel the consumer task
    cons_task.cancel()

    print("All tasks processed.")

if __name__ == "__main__":
    asyncio.run(main())
