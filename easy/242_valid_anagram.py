"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or 
phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            count_table_s = {}
            count_table_t = {}
            for i in range(len(s)):
                if s[i] not in count_table_s:
                    count_table_s[s[i]] = 1
                else:
                    count_table_s[s[i]] += 1
                if t[i] not in count_table_t:
                    count_table_t[t[i]] = 1
                else:
                    count_table_t[t[i]] += 1
            return count_table_s == count_table_t

print(Solution.isAnagram(Solution(), s="anagram", t="gramana"))