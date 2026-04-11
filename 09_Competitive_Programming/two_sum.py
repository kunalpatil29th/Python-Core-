# two_sum.py

"""
Problem: Two Sum
Given an array of integers 'nums' and an integer 'target', return indices of the two numbers such that they add up to target.
"""

def two_sum(nums, target):
    prev_map = {} # val : index
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i

# Example
nums = [2, 7, 11, 15]
target = 9
print(f"Indices for target {target}: {two_sum(nums, target)}")
