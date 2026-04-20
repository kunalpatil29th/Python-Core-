# memory_profiling.py

"""
Definition: Memory profiling is the process of measuring and analyzing the memory usage 
of a Python program. This involves tracking how much memory is allocated and deallocated 
by different parts of the code to identify memory leaks and optimize resource usage. 
The built-in module 'tracemalloc' is used for this purpose.
"""

import tracemalloc
import time

def allocate_memory():
    """Simulates memory allocation."""
    print("Allocating memory...")
    # Create a large list of strings
    data = [str(i) for i in range(100000)]
    return data

def main():
    # Start tracking memory allocations
    tracemalloc.start()
    
    # Capture the initial state
    snapshot1 = tracemalloc.take_snapshot()
    
    # Run the function that allocates memory
    memory_heavy_data = allocate_memory()
    
    # Capture the second state
    snapshot2 = tracemalloc.take_snapshot()
    
    # Compare the two snapshots
    top_stats = snapshot2.compare_to(snapshot1, 'lineno')
    
    print("\n[Memory Profiling Stats (Top 5 Difference)]")
    for stat in top_stats[:5]:
        print(stat)
        
    # Get current and peak memory usage
    current, peak = tracemalloc.get_traced_memory()
    print(f"\nCurrent memory usage: {current / 10**6:.2f} MB")
    print(f"Peak memory usage: {peak / 10**6:.2f} MB")
    
    # Stop tracking
    tracemalloc.stop()

if __name__ == "__main__":
    main()
