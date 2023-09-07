"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
"""

# runtime: 84.93% 
# memory: 62.55%
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

# time exceed
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        set = []
        for i in nums:
            if i not in set:
                set.append(i)
            else:
                return True
        return False
                
                


print(Solution.containsDuplicate(Solution(), [1, 2, 2, 3]))
print(Solution.containsDuplicate(Solution(), [1, 4, 2, 3]))
        