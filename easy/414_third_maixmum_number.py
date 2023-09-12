"""
https://leetcode.com/problems/third-maximum-number/
Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same 
value).
The third distinct maximum is 1.
"""

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        if len(set(nums)) <= 2:
            return max(nums)
        else:
            max1 = max(nums)
            max2 = max([i for i in nums if i != max1])
            max3 = max([i for i in nums if i != max1 and i != max2])
        return max3
    
print(Solution.thirdMax(Solution(), nums = [2,2,3,1]))
print(Solution.thirdMax(Solution(), nums = [1, 2]))