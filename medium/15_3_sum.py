# https://leetcode.com/problems/3sum/

# 2 sum
# [1, 2, 3, 4, 2, 4] 
# target = 6

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        for i in range(len(nums) - 1):
            target = -nums[i]
            table = set()
            for j in range(i + 1, len(nums)):
                if target - nums[j] in table:
                    temp = sorted([nums[i], nums[j], -(nums[i] + nums[j])])
                    if  temp not in output:
                        output.append(temp)
                else:
                    table.add(nums[j])
        return output
    
print(Solution.threeSum(Solution(), nums = [-1,0,1,2,-1,-4]))
                



        