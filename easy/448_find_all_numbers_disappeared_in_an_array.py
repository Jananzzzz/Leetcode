"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
"""

# don't use reserved keywords in programming
# in set is much quicker than in list
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        new_list = [i for i in range(1, len(nums) + 1)]
        return list(set(new_list).difference(set(nums)))