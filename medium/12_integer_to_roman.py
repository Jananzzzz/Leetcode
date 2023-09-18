# https://leetcode.com/problems/integer-to-roman/description/


# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        res += "M" * int(num/1000)
        num %= 1000
        if num >= 900:
            res += "CM"
            num -= 900
        if num >= 500:
            res += "D"
            num -= 500
        if num >= 400:
            res += "CD"
            num -= 400
        res += "C" * int(num/100)
        num %= 100
        if num >= 90:
            res += "XC"
            num -= 90
        if num >= 50:
            res += "L"
            num -= 50
        if num >= 40:
            res += "XL"
            num -= 40
        res += "X" * int(num/10)
        num %= 10
        if num >= 9:
            res += "IX"
            num -= 9
        if num >= 5:
            res += "V"
            num -= 5
        if num >= 4:
            res += "IV"
            num -=4
        res += "I" * num
        return res

print(Solution.intToRoman(Solution(), 58))