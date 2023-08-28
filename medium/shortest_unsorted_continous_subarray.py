"""
Given an integer array nums, you need to find one continuous subarray such that 
if you only sort this subarray in non-decreasing order, 
then the whole array will be sorted in non-decreasing order.
Return the shortest such subarray and output its length.

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array 
sorted in ascending order.
"""

# brute force with long runtime and consuming large memory`
class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        start = 0
        end = 0
        for i in range(len(nums)):
            if nums[i] <= min(nums[i:]):
                start += 1
            else:
                break
        for j in range(len(nums)-1):
            if nums[len(nums)-j-1] >= max(nums[:len(nums)-j-1]):
                end += 1
            else:
                break
        return len(nums) - start - end if (len(nums) - start - end) >= 0 else 0
    
print(Solution.findUnsortedSubarray(Solution(), nums = [2,6,4,8,10,9,15]))
print(Solution.findUnsortedSubarray(Solution(), nums = [1,2,3,4]))
print(Solution.findUnsortedSubarray(Solution(), nums = [1,2]))
print(Solution.findUnsortedSubarray(Solution(), nums = [1]))
print(Solution.findUnsortedSubarray(Solution(), nums = [9,1]))