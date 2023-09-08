"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count_table = {}
        for i in nums:
            if i not in count_table:
                count_table[i] = 1
            else:
                count_table[i] += 1
        rank_list = sorted(count_table.items(), key=lambda x: x[1], reverse=True)
        return rank_list[0][0]

print(Solution.majorityElement(Solution(), [2, 2, 1, 1, 1, 1]))
print(Solution.majorityElement(Solution(), [3, 2, 1, 2]))