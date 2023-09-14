# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b_string = bin(n)[2:].lstrip()
        for i in range(len(b_string)):
            if i%2 == int(b_string[i]):
                return False
        return True

print(Solution.hasAlternatingBits(Solution(), 7))
print(Solution.hasAlternatingBits(Solution(), 5))

