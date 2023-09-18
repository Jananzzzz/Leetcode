# https://leetcode.com/problems/longest-palindromic-substring/description/

# ababcdddmmscscs

# brute force: time limit exceed
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

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
    

print(Solution.longestPalindrome(Solution(), s="ababc"))
print(Solution.longestPalindrome(Solution(), s="cbbd"))
print(Solution.longestPalindrome(Solution(), s="aa"))


