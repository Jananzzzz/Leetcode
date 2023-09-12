"""
https://leetcode.com/problems/base-7/
Given an integer num, return a string of its base 7 representation.

Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
"""

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = [] 
        sign = "-" if num < 0 else ""
        num = abs(num)
        while(num > 0):
            res.append(str(num % 7))
            num //= 7
        res.append(sign)
        res.reverse()
        res = ''.join(res)
        return res

print(Solution.convertToBase7(Solution(), 100))
        