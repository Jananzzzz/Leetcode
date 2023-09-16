# https://leetcode.com/problems/number-of-lines-to-write-string/description/

class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        res = 1
        count = 0
        for i in s:
            count += widths[ord(i) - ord('a')]
            if count > 100:
                res += 1
                count = widths[ord(i) - ord('a')]
        
        return [res, count]