# https://leetcode.com/problems/degree-of-an-array/

from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        nums_set = set(nums)
        table = defaultdict(list)
        for i in nums_set:
            table[nums.count(i)].append(i)
        min_len = len(nums)
        
        list_of_keys = list(table.keys())
        max_of_keys = max(list_of_keys)
        for i in table[max_of_keys]:
            temp = abs(nums.index(i) - len(nums) + nums[::-1].index(i))
            min_len = min(min_len, temp)
        
        return min_len
    
print(Solution.findShortestSubArray(Solution(), nums = [1,2,2,3,1]))
print(Solution.findShortestSubArray(Solution(), nums = [1,2,2,3,1,4,2]))