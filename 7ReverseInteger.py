class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x >= 0:
            s = str(x)
            for i in range(len(s)):
                res += int(s[i])*(10**i)
            if res > 2**31 -1:
                return 0 
            return res
        if x < 0:
            s = str(-x)
            for i in range(len(s)):
                res += int(s[i])*(10**i)
            res = -res
            if res < -2**31:
                return 0 
            return res