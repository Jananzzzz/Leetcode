"""
https://leetcode.com/problems/perfect-number/
A perfect number is a positive integer that is equal to the sum of its positive divisors, 
excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
Example 2:

Input: num = 7
Output: false
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 6:
            return False
        divisors = []
        for i in range(1, num//2 + 1):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors) == num
    
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0
        for i in range(1,  num):
            if num % i == 0 and i * i <= num:
                sum += i
                if i != 1:
                    sum += num/i
            if i * i > num:
                break
        return sum == num

print(Solution.checkPerfectNumber(Solution(), 6))
print(Solution.checkPerfectNumber(Solution(), 36))
print(Solution.checkPerfectNumber(Solution(), 28))
        