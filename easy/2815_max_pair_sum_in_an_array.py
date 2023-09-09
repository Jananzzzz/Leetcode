"""
You are given a 0-indexed integer array nums. You have to find the maximum sum of a pair of 
numbers from nums such that the maximum digit in both numbers are equal.

Return the maximum sum or -1 if no such pair exists.

Example 1:

Input: nums = [51,71,17,24,42]
Output: 88
Explanation: 
For i = 1 and j = 2, nums[i] and nums[j] have equal maximum digits with a pair sum of 71 + 17 = 88. 
For i = 3 and j = 4, nums[i] and nums[j] have equal maximum digits with a pair sum of 24 + 42 = 66.
It can be shown that there are no other pairs with equal maximum digits, so the answer is 88.
Example 2:

Input: nums = [1,2,3,4]
Output: -1
Explanation: No pair exists in nums with equal maximum digits.
"""

# bad problem with unclear descriptions

class Solution:
    def maxSum(self, nums: list[int]) -> int:
        table = {}
        ans = 0

        for i in nums:
            max_digit = int(max(str(i)))
            if max_digit in table:
                table[max_digit].append(i)
            else:
                table[max_digit] = [i]
        
        for i in table:
            if len(table[i]) > 1:
                table[i].sort()
                ans = max(ans, table[i][-1] + table[i][-2])
        
        return -1 if ans == 0 else ans

print(Solution.maxSum(Solution(), nums = [51,71,17,24,42]))