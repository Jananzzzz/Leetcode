"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = True
        new_s = ""
        for i in s:
            if ("a"<=i<="z") or ("A"<=i<="Z") or ("0"<=i<="9"):
                new_s += i
        new_s = new_s.lower()
        for i in range(len(new_s)//2):
            if new_s[i] != new_s[-(i+1)]:
                ans = False
        return ans

print(Solution.isPalindrome(Solution(), s = "A man, a plan, a canal: Panama"))
