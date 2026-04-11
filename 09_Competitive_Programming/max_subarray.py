# max_subarray.py

"""
Problem: Maximum Subarray (Kadane's Algorithm)
Find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""

def max_sub_array(nums):
    max_sum = nums[0]
    cur_sum = 0
    for n in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += n
        max_sum = max(max_sum, cur_sum)
    return max_sum

# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Maximum subarray sum: {max_sub_array(nums)}")
