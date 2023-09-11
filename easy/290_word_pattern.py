"""
https://leetcode.com/problems/word-pattern/
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern 
and a non-empty word in s.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = {}
        s_list = s.split(" ")
        if len(pattern) != len(s_list):
            return False
        else:
            for i in range(len(pattern)):
                if pattern[i] not in table:
                    table[pattern[i]] = s_list[i]
                else:
                    if table[pattern[i]] != s_list[i]:
                        return False
        original_list = list(table.values())
        distinct_list = list(set(original_list))
        return len(original_list) == len(distinct_list)
    
print(Solution.wordPattern(Solution(), pattern = "abba", s = "dog cat cat dog"))
print(Solution.wordPattern(Solution(), pattern = "abba", s = "dog cat cat fish"))