"""
Given an integer array nums and an integer k, return the number of subarrays of nums
 where the greatest common divisor of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The greatest common divisor of an array is the largest integer 
that evenly divides all the array elements.

Example 1:

Input: nums = [9,3,1,2,6,3], k = 3
Output: 4
Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
- [9,3,1,2,6,_3]
- [9,3,1,2,_6,_3]
- [_9,_3,1,2,6,3]
- [9,_3,1,2,6,3]
"""

# brute force method (exceed time limit)
class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                test_nums = nums[i:j]
                if self.greatest_common_divisor(test_nums, k) == k:
                    # print(nums[i:j])
                    ans += 1
        return ans

    def greatest_common_divisor(self,nums: list[int], k: int):
        if min(nums)%k != 0:
            return -100
        gcd = min(nums)
        while(gcd > 0):
            for i in range(len(nums)):
                if nums[i]%gcd != 0:
                    gcd -= 1
                    break
                if i == len(nums) - 1:
                    return gcd
                
# brute force with better implemention (optimization)
# self-implemented gcd function much slower than math.gcd package
class Solution:
    def subarrayGCD(self, nums: list[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i, len(nums)):
                temp = self.greatest_common_divisor(temp, nums[j])
                if temp == k:
                    ans += 1
                elif temp < k:
                    break
        return ans

    def greatest_common_divisor(self, num1: int, num2: int) -> int:
        while(min(num1, num2) > 0):
            temp1 = num1
            temp2 = num2
            num1 = abs(temp1 - temp2)
            num2 = min(temp1, temp2)
        return num2
    

# print(Solution.greatest_common_divisor(Solution(), [12, 14, 12], 12))

# print(Solution.greatest_common_divisor(Solution(), 24, 36))

test2 = Solution()
result = test2.subarrayGCD([5,1,15,11,12,14,12,9], 12)
expected = 2
print(result == expected, ", your result of test2: ", result, ", expected: ", expected)
                    
test0 = Solution()
result = test0.subarrayGCD([9, 3, 1, 2, 6, 3], 3)
expected = 4
print(result == expected, ", your result of test0: ", result, ", expected: ", expected)

test1 = Solution()
result = test1.subarrayGCD([3, 12, 9, 6], 3)
expected = 7
print(result == expected, ", your result of test1: ", result, ", expected: ", expected)


                
                