"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
"""
# Solution goes below
from typing import List
class Solution:
    # brute force solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    # optimized solution using hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_maps = {}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in nums_maps:
                return [nums_maps[remain], i]
            nums_maps[nums[i]] = i
        return []

# testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))  # Output: [0,1]
    print(sol.twoSum([3,2,4], 6))      # Output: [1,2]
    print(sol.twoSum([3,3], 6))        # Output: [0,1]
