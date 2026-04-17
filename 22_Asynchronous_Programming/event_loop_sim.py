# event_loop_sim.py

"""
Definition: The event loop is the core of every asyncio application. It runs asynchronous tasks and callbacks, performs network I/O operations, and runs subprocesses.
"""

def simulate_event_loop():
    print("Loop Status: RUNNING")
    print("  - Scheduling Coroutine A")
    print("  - Scheduling Coroutine B")
    print("  - Polling for I/O events...")
    print("  - Executing Coroutine B callback")
    print("Loop Status: IDLE")

simulate_event_loop()
