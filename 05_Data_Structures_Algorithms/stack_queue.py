# stack_queue.py

"""
Definition: 
Stack: A LIFO (Last-In-First-Out) data structure where elements are added and removed from the same end.
Queue: A FIFO (First-In-First-Out) data structure where elements are added at one end and removed from the other.
"""

# Stack implementation using a list
stack = []
stack.append(1)  # push
stack.append(2)
stack.append(3)
print("Stack:", stack)
print("Popped from stack:", stack.pop())
print("Stack after pop:", stack)

# Queue implementation using collections.deque
from collections import deque
queue = deque()
queue.append("A")  # enqueue
queue.append("B")
queue.append("C")
print("\nQueue:", list(queue))
print("Dequeued from queue:", queue.popleft())
print("Queue after dequeue:", list(queue))
