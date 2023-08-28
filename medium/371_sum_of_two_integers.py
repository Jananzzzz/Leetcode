"""
Given two integers a and b, return the sum of the two integers 
without using the operators + and -.
Example 1:

Input: a = 1, b = 2
Output: 3

Constraints:
-1000 <= a, b <= 1000
"""

"""
not finished yet, require bit level operation
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        sticks = [0] * 2000
        if a >= 0:
            sticks.extend([0] * a)
        else:
            for i in range(abs(a)):
                sticks.pop()
        if b >= 0:
            sticks.extend([0] * b)
        else:
            for i in range(abs(b)):
                sticks.pop()
        if len(sticks) >= 2000:
            for i in range(2000):
                sticks.pop()
            return len(sticks)
        else:
            pass


test0 = Solution()
result = test0.getSum(20, -30)
print(result)

