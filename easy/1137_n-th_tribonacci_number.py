"""
https://leetcode.com/problems/n-th-tribonacci-number/?envType=study-plan-v2&envId=leetcode-75
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537

[0, 1, 1, 2, 4, 7, 13, 24, 44, 81, ...]
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        f = [0, 1, 1]
        if n <= 2:
            return f[n]
        for i in range(3, n+1):
            f.append(f[0] + f[1] + f[2])
            f[0] = f[1]
            f[1] = f[2]
            f[2] = f[3]
            f.pop()
        return f[2]

print(Solution.tribonacci(Solution(), 25))
