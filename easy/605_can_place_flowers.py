"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, 
flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the 
no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 1: 
                return n <= 0
            else:
                return n <= 1
        count = 0
        if flowerbed[0] == flowerbed[1] == 0:
            flowerbed[0] = 1
            count += 1
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
        if flowerbed[-2] == flowerbed[-1] == 0:
            flowerbed[-1] = 1
            count += 1
        return count >= n

print(Solution.canPlaceFlowers(Solution(), flowerbed = [0], n = 1))
print(Solution.canPlaceFlowers(Solution(), flowerbed = [1,0,0,0,1], n = 1))
print(Solution.canPlaceFlowers(Solution(), flowerbed = [1,0,0,0,1], n = 2))

            

            