# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        prime_number = [2, 3, 5, 7, 11, 13, 17, 19]
        for i in range(left, right+1):
            b_i = bin(i)[2:].count('1')
            if b_i in prime_number:
                res += 1
        