# contains_duplicate.py

"""
Problem: Contains Duplicate
Given an integer array 'nums', return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

def contains_duplicate(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

# Example
nums = [1, 2, 3, 1]
print(f"Does {nums} contain duplicates? {contains_duplicate(nums)}")
