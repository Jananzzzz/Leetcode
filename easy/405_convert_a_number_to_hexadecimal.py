"""
https://leetcode.com/problems/convert-a-number-to-hexadecimal/
Given an integer num, return a string representing its hexadecimal representation. 
For negative integers, two’s complement method is used.
All the letters in the answer string should be lowercase characters, 
and there should not be any leading zeros in the answer except for the zero itself.
Note: You are not allowed to use any built-in library method to directly solve this problem.

Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"
"""

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        elif num < 0:
            num = num + (1<<32)
        res = []
        while(num > 0):
            if num%16 < 10:
                res.append(str(num%16))
            elif num%16 == 10:
                res.append('a')
            elif num%16 == 11:
                res.append('b')
            elif num%16 == 12:
                res.append('c')
            elif num%16 == 13:
                res.append('d')
            elif num%16 == 14:
                res.append('e')
            else:
                res.append('f')
            num //= 16
        res.reverse()
        return ''.join(res)
    
print(Solution.toHex(Solution(), num=26))
print(Solution.toHex(Solution(), num=16))
