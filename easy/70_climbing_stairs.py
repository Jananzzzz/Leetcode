"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# recursion
# f(0) = 1
# f(1) = 1
# f(2) = 2
# f(3) = 3
class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev2 = 1
        temp = 0
        for i in range(1, n):
            temp = prev2
            prev2 += prev1
            prev1 = temp
        return prev2

# print(Solution.climbStairs(Solution(), 2))  # 2
print(Solution.climbStairs(Solution(), 3))
print(Solution.climbStairs(Solution(), 4))

        