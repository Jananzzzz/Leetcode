# https://leetcode.com/problems/regular-expression-matching/

"""
abcaaaacds
abca**aacds

abcd
a*bcd
"""

# recursion with time limit exceed
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        
        first_match = bool(s) and p[0] in [s[0], '.']

        if len(p) >= 2 and p[1] == '*':
            # return (self.isMatch(s, p[2:]) or
            #         first_match and self.isMatch(s[1:], p))
            if not first_match:
                return self.isMatch(s, p[2:])
            else:
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)

        else:
            return first_match and self.isMatch(s[1:], p[1:])

# optimize with cache:
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}
        
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if (j + 1) < len(p) and p[j + 1] == '*':
                cache[(i, j)] = (dfs(i, j + 2) or
                                 (match and dfs(i + 1, j)))
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return cache[(i, j)]
        
        return dfs(0, 0)

        
# print(Solution.isMatch(Solution(), s='abcd', p='a*bcd'))
print(Solution.isMatch(Solution(), s='abcd', p='.*d'))
print(Solution.isMatch(Solution(), s='abcd', p='aabcd'))