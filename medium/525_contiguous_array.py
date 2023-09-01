"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number 
of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]

Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""


# simple idea exceeding time limits
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
            elif nums[i] == 1:
                continue
            else:
                nums[i] = 0
        # print(nums)
        max_len = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)+1):
                if (sum(nums[i:j]) == 0) & ((j-i) > max_len):
                # bad style with wrong results
                # if (sum(nums[i:j]) == 0) & (j-i) > max_len:
                    max_len = j - i
        return max_len
    

# optimized, still exceed time limit
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        max_len = 0
        for i in range(len(nums)-1):
            j = len(nums)
            if j - i <= max_len:
                break
            while((i+1+max_len) < j):
                # if (sum(nums[i:j]) == 0) & ((j-i) > max_len):
                if (nums[i:j].count(0) == nums[i:j].count(1)):
                    max_len = j - i
                    break
                j -= 1
        return max_len
    
# hash map o(n)
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        table = {0: -1}
        max_len = 0
        count = 0
        for idx, i in enumerate(nums):
            if i == 1:
                count += 1
            elif i == 0:
                count -= 1
            if count in table:
                max_len = max(max_len, idx - table[count])
            else:
                table[count] = idx 
        return max_len
        

print(Solution.findMaxLength(Solution(), [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]))
print(Solution.findMaxLength(Solution(), [0, 1, 0, 1]))
print(Solution.findMaxLength(Solution(), [1, 2, 3, 0, 1]))