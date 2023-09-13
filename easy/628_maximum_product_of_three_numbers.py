"""
https://leetcode.com/problems/maximum-product-of-three-numbers/
Given an integer array nums, find three numbers whose product is maximum and return 
the maximum product.

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
"""

class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])

print(Solution.maximumProduct(Solution(), nums = [1,2,3,4]))
print(Solution.maximumProduct(Solution(), nums = [-1,-2,-3]))
