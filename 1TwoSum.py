"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:      # here the -> List[int] is a notation, which means the output of this function is an integer list
        for i in range(len(nums)-1):                               # List must write as list in vscode
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return([i, j])
"""
# the solution above use brute force, which exceed the time limit

# use dictionary to store all the numbers that has been test before


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return([seen[target-num], i])
            elif num not in seen:
                seen[num] = i  

'''

class Solution(object):

    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        for i in range(len(self.nums)):
            for j in range(i+1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    print "index1=" + str(i) + ", index2=" + str(j)

sample = Solution([2, 8, 7, 15], 9)
sample.twoSum()
'''