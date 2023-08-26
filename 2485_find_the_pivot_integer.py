"""
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

Example 1:

Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
"""

class Solution:
    def pivotInteger(self, n: int) -> int:
        exact_value = ((n**2 + n)/2)**(1/2)
        if exact_value == int(exact_value):
            return int(exact_value)
        else:
            return -1