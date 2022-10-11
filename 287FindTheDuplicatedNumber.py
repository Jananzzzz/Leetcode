# more clever one:
class Solution1:
    def findDuplicate(self, nums: list[int]) -> int:
        k = 0
        for i in nums:
            k += i 
        return int(-(len(nums)-1)*(len(nums))/2 + k )

# time complexity O(n)    # space complexity O(1)
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # nums = [1,3,3,2]
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            else: nums[abs(nums[i])] = -nums[abs(nums[i])]

test = Solution1
res = test.findDuplicate(test, nums=[1,3,3,2])
print(res)
# cis for change a whole part e.g. a function