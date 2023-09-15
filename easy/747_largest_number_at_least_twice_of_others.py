# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        temp = sorted(nums)
        if temp[-1] >= 2*temp[-2]:
            return nums.index(temp[-1])
        return -1