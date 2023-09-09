"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = {}
        for i in magazine:
            if i not in table:
                table[i] = 1
            else:
                table[i] += 1
        for j in ransomNote:
            if j not in table:
                return False
            else:
                table[j] -= 1
                if table[j] < 0:
                    return False
        return True

print(Solution.canConstruct(Solution(), ransomNote = "aa", magazine = "aab"))
print(Solution.canConstruct(Solution(), ransomNote = "aa", magazine = "ab"))