# https://leetcode.com/problems/longest-continuous-increasing-subsequence

class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        res = 1
        length = 1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                length += 1
            else:
                res = max(res, length)
                length = 1
        return max(res, length)
    
print(Solution.findLengthOfLCIS(Solution(), nums=[1,3,5,4,2,3,4,5]))


        