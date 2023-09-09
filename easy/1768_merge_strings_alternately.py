"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
 starting with word1. If a string is longer than the other, append the additional letters 
 onto the end of the merged string.
Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        length = max(len(word1), len(word2))
        for i in range(length):
            try:
                res += word1[i]
            except:
                pass 
            try:
                res += word2[i]
            except:
                pass
        return res

print(Solution.mergeAlternately(Solution(), word1 = "ab", word2 = "pqrs"))