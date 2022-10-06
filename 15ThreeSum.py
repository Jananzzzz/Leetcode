class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans = set()
        nums.sort()

        for i, target in enumerate(nums):
            if i > 0 and nums[i-1] == target:
                continue
            prev = set()
            for j in range(i+1, len(nums)):
                diff = -target - nums[j]
                if diff in prev:
                    ans.add((nums[j], diff, target))
                prev.add(nums[j])
        
        return ans 