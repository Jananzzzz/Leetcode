"""
https://leetcode.com/problems/reverse-string-ii/
Given a string s and an integer k, reverse the first k characters for every 2k characters 
counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k 
but greater than or equal to k characters, then reverse the first k characters and leave 
the other as original.

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
"""

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = [i for i in s]
        index = 0
        while(index < len(s)):
            if index + k <= len(s):
                s[index: index + k] = s[index: index + k][::-1]
            else:
                s[index:] = s[index:][::-1]
            index += 2 * k
        return ''.join(s)

print(Solution.reverseStr(Solution(), s = "abcdefg", k = 2))

