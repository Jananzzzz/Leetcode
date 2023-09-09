"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        if s[-1] == " ":
            for i in range(len(s)):
                if s[-i-1] != " ":
                    for j in range(i, len(s)):
                        if s[-j-1] != " ":
                            count += 1
                        else:
                            return count
                    return count
        else:
            for k in range(len(s)):
                if s[-k-1] != " ":
                    count += 1
                else:
                    return count
            return count
                
# print(Solution.lengthOfLastWord(Solution(), s="   fly me   to   the moon "))
print(Solution.lengthOfLastWord(Solution(), s="aaa   "))