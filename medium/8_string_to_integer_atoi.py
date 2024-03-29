# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0:
            return 0
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        else:
            sign = 1
        digits = []
        for c in s:
            if c.isdigit():
                digits.append(c)
            else:
                break
        if len(digits) == 0:
            return 0
        else:
            num = int(''.join(digits))
            num *= sign
        num = max(num, -2**31)
        num = min(num, 2**31 - 1)
        return num


print(Solution.myAtoi(Solution(), s='42'))