class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        exp = []
        for i in range(len(nums)):
            if nums[i] != val:
                exp.append(nums[i])
        for i in range(len(exp)):
            nums[i] = exp[i]
        return len(exp) 