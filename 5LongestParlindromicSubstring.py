# time limit exceeded version:
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def verify(string):
            reverse = string[-1::-1]
            if reverse == string:
                return True
            else:
                return False
            
        tmp = ""
        
        for i in range(1, len(s)+1):
            for j in range(0, len(s)-i+1):
                if verify(s[j: j+i]):
                    tmp = s[j: j+i]
                    break 
                else: continue 
                
        return tmp

x = Solution()
result = x.longestPalindrome("ababad")
print(result)
'''

class Solution:    
    def longestPalindrome(self, s: str) -> str:
        def countPalindromeAroundCenter(lo: int, hi: int, s: str):
            res1 = ""
            while lo >= 0 and hi < len(s):
                if s[lo] != s[hi]:
                    break
                lo -= 1
                hi += 1
            res1 = s[(lo+1): hi]
            return res1
        
        res = "" 
        for i in range(len(s)):
            a = countPalindromeAroundCenter(i, i, s)
            b = countPalindromeAroundCenter(i, i+1, s)
            if len(a) > len(res):
                res = a
            if len(b) > len(res):
                res = b
        
        return res