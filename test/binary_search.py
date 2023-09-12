import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # return int((-1+math.sqrt(1+8*n))/2) # solve inequation
        pass

print(Solution.arrangeCoins(Solution(), 5))
print(Solution.arrangeCoins(Solution(), 8))
print(Solution.arrangeCoins(Solution(), 55))
print(Solution.arrangeCoins(Solution(), 56))

"""
i * (i + 1) < 2n <= (i + 1) * (i + 2)
"""