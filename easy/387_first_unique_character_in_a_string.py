"""
https://leetcode.com/problems/first-unique-character-in-a-string/
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        for key in count.keys():
            if count[key] == 1:
                return s.index(key)
        return -1
    
print(Solution.firstUniqChar(Solution(), s="aabb"))
print(Solution.firstUniqChar(Solution(), s="leetcode"))
print(Solution.firstUniqChar(Solution(), s="loveleetcode"))
        