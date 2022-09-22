"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:      # here the -> List[int] is a notation, which means the output of this function is an integer list
        for i in range(len(nums)-1):                               # List must write as list in vscode
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return([i, j])
"""
# the solution above use brute force, which exceed the time limit

