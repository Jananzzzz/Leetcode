"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value 
and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_avg = 0
        for i in range(k):
            max_avg += nums[i]
        temp = max_avg
        for i in range(1, len(nums)-k+1):
            temp += nums[i+k-1] - nums[i-1]
            max_avg = max(max_avg, temp)
        return max_avg/k


print(Solution.findMaxAverage(Solution(), nums = [5], k = 1))
print(Solution.findMaxAverage(Solution(), nums = [1,12,-5,-6,50,3], k = 4))
            

        