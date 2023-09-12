"""
https://leetcode.com/problems/number-complement/description/
The complement of an integer is the integer you get when you flip all the 0's to 1's and
 all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the 
integer 2.
Given an integer num, return its complement.

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), 
and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), 
and its complement is 0. So you need to output 0.
"""

class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        exp = 0
        while True:
            if 2 ** exp <= num < 2 ** (exp + 1):
                return 2 ** (exp + 1) - 1 - num
            else:
                exp += 1

class Solution:
    def findComplement(self, num: int) -> int:
        exp = 0
        while True:
            if num >= 2 ** exp:
                exp += 1
            else:
                return 2 ** exp - 1 - num

class Solution:
    def findComplement(self, num: int) -> int:
        b_num = bin(num)[2:].lstrip('0')
        print(b_num)
        temp = [str(1-int(i)) for i in b_num]
        complement = ''.join(temp)
        return int(complement, 2)