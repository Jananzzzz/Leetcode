# format transform a number to a string
# a = "111"
# int(a, 2) == 7

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), "b")
        