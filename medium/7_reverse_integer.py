# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        x_str = str(x) if x > 0 else str(-x)
        x_str = x_str[::-1]
        if x != 0:
            x_str = x_str.lstrip('0')
        res =  int("-" + x_str) if x < 0 else int(x_str)
        return res if res in range(-2**31, 2**31 - 1) else 0

print(Solution.reverse(Solution(), x=123))
print(Solution.reverse(Solution(), x=-12))
print(Solution.reverse(Solution(), x=-120))