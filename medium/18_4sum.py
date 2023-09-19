# https://leetcode.com/problems/4sum/description/

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        def twoSum(nums: list[int], target: int) -> list[list[int]]:
            res = []
            s = set()
            for i in range(len(nums)):
                if target - nums[i] in s:
                    res.append([target - nums[i], nums[i]])
                else:
                    s.add(nums[i])
            return res
        
        def kSum(nums: list[int], target: int, k: int) -> list[list[int]]:
            res = []
            
            if not nums:
                return res
            
            # there are k remaining values to be add to the sum.
            # the average of these values is at least target // k

            average_value = target // k

            # return if the smallest value > average_value
            # or greatest value < average_value
            if average_value > nums[-1] or average_value < nums[0]:
                return res
            
            if k == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]: # avoid duplicate
                    for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                        # print(subset)
                        res.append([nums[i]] + subset)
            return res
        
        nums.sort()
        return kSum(nums, target, 4)

print(Solution.fourSum(Solution(), nums=[1,0,-1,0,-2,2], target=0))
            


        