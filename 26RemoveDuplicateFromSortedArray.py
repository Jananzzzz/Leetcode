class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        exp = [nums[0]]

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                exp.append(nums[i+1])
        for i in range(len(exp)):
            nums[i] = exp[i]
        return len(exp)