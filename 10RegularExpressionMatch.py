'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        text = s
        pattern = p
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            #return first_match and self.isMatch(text[1:], pattern)
            
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])
'''
# dynamic programming: without extra space for new-created text and pattern string.
        # "asd ddd amdk"
        # "asd  *  amdk"
        # "aa"
        # "a*a"
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        text = s
        pattern = p
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:            
                if j == len(pattern):            # compare to the end, then stop
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[(i, j)] = ans
            
                
            return memo[(i, j)]

        return dp(0, 0)