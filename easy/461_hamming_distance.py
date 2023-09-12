"""
https://leetcode.com/problems/hamming-distance/description/
The Hamming distance between two integers is the number of positions at which 
the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        b_x = (32 - len(bin(x)[2:])) * '0' + bin(x)[2:]
        b_y = (32 - len(bin(y)[2:])) * '0' + bin(y)[2:]
        return sum([1 for i in range(32) if b_x[i] != b_y[i]])