"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        index = 0
        for i in range(len(s)):
            if (len(t) - index) < (len(s) - i):
                return False
            for j in range(index, len(t)):
                if t[j] == s[i]:
                    index += (j - index + 1)
                    break
                if (j == len(t) - 1) and (t[j] != s[i]):
                    return False
        return True

# print(Solution.isSubsequence(Solution(), s = "abc", t = "ahbgdc"))
# print(Solution.isSubsequence(Solution(), s = "axc", t = "ahbgdc"))
print(Solution.isSubsequence(Solution(), s = "acb", t = "ahbgdc"))
# print(Solution.isSubsequence(Solution(), s = "twn", t = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn"))
            
