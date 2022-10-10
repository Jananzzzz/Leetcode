class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        k = len(palindrome)>>1

        for i in range(k):
            if palindrome[i] != 'a':
                # palindrome[i] = 'a'
                return palindrome[:i] + 'a' + palindrome[i+1:]

        return palindrome[:-1] + 'b'