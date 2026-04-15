# caching_strategy.py

"""
Definition: Caching is the process of storing data in a temporary storage area (cache) so that future requests for that data can be served faster.
"""

import time

class SimpleCache:
    def __init__(self):
        self.store = {}

    def get_data(self, key):
        if key in self.store:
            print("Fetching from Cache...")
            return self.store[key]
        
        print("Computing data (expensive operation)...")
        time.sleep(1) # Simulate delay
        result = f"Result for {key}"
        self.store[key] = result
        return result

# Usage
cache = SimpleCache()
print(cache.get_data("item1"))
print(cache.get_data("item1")) # Should be instant
