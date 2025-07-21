"""
LeetCode

TwoSum Solution
"""

# Returns the indices of two numbers (from a list of numbers labeled nums) that add up to an integer target. 
def two_sum(nums, target):
    # Creates an inverted dictionary where the values are indices. This allows a solution of O(n) time.
    nums_indexed = {value: index for index, value in enumerate(nums)}
    for i in range(len(nums)):
        complement = target - nums[i]
        # Ensures indices are unique, weeding out duplicate solutions.
        if complement in nums_indexed and i != nums_indexed[complement]:
            return [i, nums_indexed[complement]]
    return [] # Explicitly returns an empty list when no solution is found.
