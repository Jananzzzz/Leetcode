"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/
Given a string s, reverse the order of characters in each word within a sentence while still 
preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        res = ""
        for i in s_list:
            i_list = [j for j in i]
            i_list.reverse()
            i_reverse = ''.join(i_list)
            res += i_reverse
            res += ' '
        return res[:-1]
    
print(Solution.reverseWords(Solution(), s = "Let's take LeetCode contest"))