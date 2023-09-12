"""
https://leetcode.com/problems/add-strings/
Given two non-negative integers, num1 and num2 represented as string, 
return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers 
(such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        min_len = min(len(num1), len(num2))
        carrier = 0
        res = []
        for i in range(min_len):
            temp = int(num1[-i-1]) + int(num2[-i-1]) + carrier
            if temp >= 10:
                carrier = 1
                res.append(str(temp%10))
            else:
                carrier = 0
                res.append(str(temp))
        extra_len = max(len(num1), len(num2)) - min_len
        extra = num1[:extra_len] if len(num1) > len(num2) else num2[:extra_len]
        for i in range(extra_len):
            temp = int(extra[-i-1]) + carrier
            if temp >= 10:
                carrier = 1
                res.append(str(temp%10))
            else:
                carrier = 0
                res.append(str(temp))
        if carrier != 0:
            res.append(str(carrier)) 
        res.reverse()
        return ''.join(res)

print(Solution.addStrings(Solution(), num1 = "0", num2 = "0"))
print(Solution.addStrings(Solution(), num1 = "11", num2 = "123"))
        