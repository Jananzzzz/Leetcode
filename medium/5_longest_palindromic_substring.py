# https://leetcode.com/problems/longest-palindromic-substring/description/

# ababcdddmmscscs

# brute force: time limit exceed 
# time complexity: n^3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_list = [i for i in s]
        max_len = 0
        max_string = ""
        for i in range(len(s_list)):
            for j in range(i, len(s_list)+1):
                if j - i > max_len:
                    if s_list[i:j] == s_list[i:j][::-1]:
                        max_len = j - i
                        max_string = ''.join(s_list[i:j])
        return max_string

# palindrome from the center
# time complexity: n^2
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0

        for i in range(len(s)):

            # odd length            
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_len:
                    res = s[left: right + 1]
                    max_len = right - left + 1
                left -=  1
                right += 1
            
            # even length
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > max_len:
                    res = s[left: right + 1]
                    max_len = right - left + 1
                left -= 1
                right += 1
        
        return res
            

                

    

print(Solution.longestPalindrome(Solution(), s="ababc"))
print(Solution.longestPalindrome(Solution(), s="cbbd"))
print(Solution.longestPalindrome(Solution(), s="aa"))


