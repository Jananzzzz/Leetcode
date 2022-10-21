from tkinter import N


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # nums = [2, 3, 5, 4, 3, 5]  k = 2
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                if i - dic[nums[i]] <= k:
                    return True
                else: 
                    dic[nums[i]] = i
        return False
