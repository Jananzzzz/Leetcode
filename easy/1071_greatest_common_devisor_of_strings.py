"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
(i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides 
both str1 and str2.

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        max = 0
        min_len = min(len(str1), len(str2))
        for i in range(min_len):
            if (str1 == int(len(str1)/(i+1)) * str1[:i+1]) and (str2 == int(len(str2)/(i+1)) * str1[:i+1]):
                max = i+1
        return str1[:max] if max > 0 else ""

print(Solution.gcdOfStrings(Solution(), str1 = "ABABAB", str2 = "ABAB"))
print(Solution.gcdOfStrings(Solution(), str1 = "LEET", str2 = "CODE"))