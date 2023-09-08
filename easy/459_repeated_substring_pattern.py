"""
Given a string s, check if it can be constructed by taking a substring of it and 
appending multiple copies of the substring together.

Example 1:

Input: s = "abab"
Output: true

Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s == (len(s)//(i+1)) * s[:i+1]:
                return True
        return False
    
print(Solution.repeatedSubstringPattern(Solution(), "abcabcabcabc"))
print(Solution.repeatedSubstringPattern(Solution(), "aba"))
                