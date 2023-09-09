"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = int(a, 2) + int(b, 2)
        return bin(res)[2:]

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carrier = 0
        res = []
        min_len = min(len(a), len(b))
        for i in range(min_len):
            temp = int(a[-i-1]) + int(b[-i-1]) + carrier
            if temp <= 1:
                carrier = 0
                res.append(temp)
            else:
                carrier = 1
                res.append(temp%2)
        remain = a[:abs(len(a) - len(b))] if (len(a) > len(b)) else b[:abs(len(a) - len(b))]
        for i in range(len(remain)):
            temp = int(remain[-i-1]) + carrier
            if temp <= 1:
                carrier = 0
                res.append(temp)
            else:
                carrier = 1
                res.append(temp%2)
        if carrier == 1:
            res.append(1)
        res.reverse()
        ans = ""
        for i in res:
            ans += str(i)
        return ans

print(Solution.addBinary(Solution(), a = "11", b = "1"))
print(Solution.addBinary(Solution(), a = "1010", b = "1011"))
            