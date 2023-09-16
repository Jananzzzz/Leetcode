# https://leetcode.com/problems/positions-of-large-groups/description/

class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        res = []
        start = 0
        for i in range(len(s)-1):
            if s[i+1] != s[i]:
                if i - start >= 2:
                    res.append([start, i])
                start = i + 1
        if len(s) - 1 - start >= 2:
            res.append([start, len(s)-1])
        return res
        

        