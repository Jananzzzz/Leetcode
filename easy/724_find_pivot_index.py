"""
https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of 
the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because 
there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        right = sum(nums) - nums[0]
        if left == right:
            return 0
        for i in range(1, len(nums)):
            left += nums[i-1]
            right -= nums[i]
            if left == right:
                return i
        return -1

print(Solution.pivotIndex(Solution(), nums = [1,2,3]))
print(Solution.pivotIndex(Solution(), nums = [1, 7, 3, 5, 6, 5]))

            
