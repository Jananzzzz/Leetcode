"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

# brute force solution with long runtime but less memory
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            s1_dict = {}
            for letter in s1:
                if letter in s1_dict:
                    s1_dict[letter] += 1
                else:
                    s1_dict[letter] = 0
            for i in range(0, len(s2)-len(s1)+1):
                sub_str = s2[i:i+len(s1)]
                sub_dict = {}
                for letter in sub_str:
                    if letter in sub_dict:
                        sub_dict[letter] += 1
                    else:
                        sub_dict[letter] = 0
                if sub_dict == s1_dict:
                    return True
            return False
        
print(Solution.checkInclusion(Solution(), "plll", "apple"))
                
                