"""
You have a set of integers s, which originally contains all the numbers from 1 to n. 
Unfortunately, due to some error, one of the numbers in s got duplicated to another number 
in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them 
in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
"""

class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        res = [0, len(nums)]
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                res[0] = nums[i]
            if i+1 not in nums:
                res[1] = i+1
        return res

            

print(Solution.findErrorNums(Solution(), nums=[1,2,2,4]))
print(Solution.findErrorNums(Solution(), nums=[3,2,3,4,6,5]))
print(Solution.findErrorNums(Solution(), nums=[1, 1]))
            

                

        