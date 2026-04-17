# threading_vs_asyncio.py

"""
Definition: 
- Threading: OS-level multitasking, good for I/O-bound tasks but has overhead.
- Asyncio: Single-threaded cooperative multitasking, extremely efficient for high-concurrency I/O.
"""

def comparison():
    print("Comparison:")
    print("  - Threading: Pre-emptive (OS decides when to switch)")
    print("  - Asyncio: Cooperative (Code decides when to yield control)")
    print("Rule of thumb: Use asyncio for network/web, threading for legacy or some blocking I/O.")

comparison()
