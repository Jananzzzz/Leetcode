# https://leetcode.com/problems/shortest-distance-to-a-character/description/

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        output = [len(s)]*len(s)
        for i in range(len(s)):
            if s[i] == c:
                for j in range(len(s)):
                    output[j] = min(output[j], abs(j-i))
        return output
