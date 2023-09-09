"""
Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count_table = {}
        for i in nums:
            if i in count_table:
                count_table.pop(i)
            else:
                count_table[i] = 1
        return list(count_table.keys())[0]

print(Solution.singleNumber(Solution(), nums = [4,1,2,1,2]))