class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)-1):
            if nums[i] == target:
                return i
            if (nums[i] < target and nums[i+1] > target):
                return i + 1
        if nums[-1] == target:
            return len(nums)-1
        if nums[-1] < target:
            return len(nums)
        if nums[0] > target:
            return 0