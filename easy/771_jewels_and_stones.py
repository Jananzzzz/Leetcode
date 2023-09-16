# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for i in jewels:
            res += stones.count(i)
        return res