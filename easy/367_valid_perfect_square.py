"""
https://leetcode.com/problems/valid-perfect-square/
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, 
it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return int(num ** 0.5) == (num ** 0.5)
    
# without using sqrt() or ** 
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        down = 0
        up =  num
        while down <= up:
            mid = (down + up)//2
            res = mid * mid
            if res == num:
                return True
            elif res < num:
                down = mid + 1
            elif res > num:
                up = mid - 1
        return False

print(Solution.isPerfectSquare(Solution(), num=14))
print(Solution.isPerfectSquare(Solution(), num=16))
print(Solution.isPerfectSquare(Solution(), num=0))
print(Solution.isPerfectSquare(Solution(), num=1))