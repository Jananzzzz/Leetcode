"""
The string s is considered an acronym of words if it can be formed by concatenating 
the first character of each string in words in order. For example, "ab" can be formed from 
["apple", "banana"], but it can't be formed from ["bear", "aardvark"].

Return true if s is an acronym of words, and false otherwise.

Example 1:

Input: words = ["alice","bob","charlie"], s = "abc"
Output: true
Explanation: The first character in the words "alice", "bob", and "charlie" are 'a', 'b', and 'c',
 respectively. Hence, s = "abc" is the acronym. 
Example 2:

Input: words = ["an","apple"], s = "a"
Output: false
Explanation: The first character in the words "an" and "apple" are 'a' and 'a', respectively. 
The acronym formed by concatenating these characters is "aa". 
Hence, s = "a" is not the acronym.
"""

class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        else:
            for i in range(len(words)):
                if words[i][0] != s[i]:
                    return False
            return True

print(Solution.isAcronym(Solution(), words = ["an","apple"], s = "a"))
print(Solution.isAcronym(Solution(), words = ["an","apple"], s = "aa"))
        