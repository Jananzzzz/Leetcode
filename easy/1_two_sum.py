"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

# brute force
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# hash table
class Solution0:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_table = {}
        for i in range(len(nums)):
            if target - nums[i] in hash_table:
                return [hash_table[target - nums[i]], i]
            else:
                hash_table[nums[i]] = i

test0 = Solution0()
print(test0.twoSum([2,7,11,15], 9))
