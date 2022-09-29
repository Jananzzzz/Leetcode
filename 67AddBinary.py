# format transform a number to a string
# a = "111"
# int(a, 2) == 7

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), "b")

# int(a, 2) tells the int() function that 'a' is a binary number
# mind that the output of in(a, 2) is a decimal number
        