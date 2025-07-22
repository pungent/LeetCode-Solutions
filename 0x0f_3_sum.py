"""
3Sum Solution

Wise Words from Pungent -> This is extremely slow and awful code (But it works so hop off)
"""

nums = [-1,0,1,2,-1,-4]
# Find triplets from a list of numbers that add up to 0 (no duplicates allowed)
def three_sum(nums):
    solution = [] # Stores triplets that sum to 0
    # Get every possible combination of triplets
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                # No duplicates via sorting
                if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in solution:
                    solution.append(sorted([nums[i], nums[j], nums[k]]))
    return solution
print(three_sum(nums))