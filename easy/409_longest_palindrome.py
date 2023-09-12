"""
https://leetcode.com/problems/longest-palindrome/
Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        count = {}
        for i in s:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        count_odd = 0
        for i in count.values():
            if i%2 == 0:
                res += i
            else:
                count_odd += 1
                res += (i - 1)
        return res + 1 if count_odd >= 1 else res
    
print(Solution.longestPalindrome(Solution(), s = "abccccdd"))
print(Solution.longestPalindrome(Solution(), s = "a"))