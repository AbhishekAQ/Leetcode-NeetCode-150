"""
Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 10^5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using division.
"""
# Solution goes below
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result
    # reducing loops
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n

        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
            postfix[i] = nums[n - i] * postfix[i - 1]

        return [prefix[i] * postfix[n - 1 - i] for i in range(0, n)]

# testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))  # Output: [24,12,8,6]
    print(sol.productExceptSelf([-1,1,0,-3,3]))  # Output: [0,0,9,0,0]