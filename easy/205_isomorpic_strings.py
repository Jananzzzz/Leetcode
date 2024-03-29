"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
 No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            map1 = []
            map2 = []
            for i in range(len(s)):
                map1.append(s.index(s[i]))
                map2.append(t.index(t[i]))
            if map1 == map2:
                return True
        return False
    
print(Solution.isIsomorphic(Solution(), s="paper", t="title"))