# https://leetcode.com/problems/self-dividing-numbers/description/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        res = []
        for i in range(left, right+1):
            nums = [int(num) for num in str(i)]
            count = 0
            if 0 in nums:
                continue
            for num in nums:
                if i%num == 0:
                    count += 1
                else:
                    break
            if count == len(nums):
                res.append(i)
        return res
    
print(Solution.selfDividingNumbers(Solution(), left = 1, right = 22))
