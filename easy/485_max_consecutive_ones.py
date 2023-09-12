"""
https://leetcode.com/problems/max-consecutive-ones/
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. 
The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        str_nums = [str(i) for i in nums]
        num_string = ''.join(str_nums)
        nums_list = num_string.split('0')
        return len(max(nums_list))
    
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_len = 0
        count = 0
        for i in nums:
            if i != 0:
                count += 1
            else:
                max_len = max(max_len, count)
                count = 0
        max_len = max(max_len, count)
        return max_len
    
print(Solution.findMaxConsecutiveOnes(Solution(), nums = [1,1,0,1,1,1]))
print(Solution.findMaxConsecutiveOnes(Solution(), nums = [1,1,1,1,1,1]))
print(Solution.findMaxConsecutiveOnes(Solution(), nums = [1,0,1,1,0,1]))