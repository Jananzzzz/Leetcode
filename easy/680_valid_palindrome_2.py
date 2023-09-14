# https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        low = 0
        high = len(s)
        while(low < high):
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                temp1 = s[:low] + s[low+1:]
                temp2 = s[:high] + s[high+1:]
                if temp1 == temp1[::-1]:
                    return True
                elif temp2 == temp2[::-1]:
                    return True
                else:
                    return False
