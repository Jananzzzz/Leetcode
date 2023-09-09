"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order
 of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""

# bad solution with long runtime and high memeory usage
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i, len(nums)):
                    if nums[j] != 0:
                        nums[j], nums[i] = nums[i], nums[j]
                        break
        return nums
    
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        index = 0
        for i in range(len(nums)):
            if  nums[i] != 0:
                nums[index] = nums[i]
                if i != index:
                    nums[i] = 0
                index += 1
        return nums

print(Solution.moveZeroes(Solution(), nums=[0, 1, 0, 3, 12]))