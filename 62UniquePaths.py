from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(m+n-2)/factorial(m-1)/factorial(n-1) )
# a DP solution:

class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for _ in range(m)] for _ in range(n)]
        if m == 1 or n == 1: return 1
        else:
            for i in range(m):
                for j in range(n):
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[-1][-1]

test = Solution
print(test.uniquePaths(test,3,4))
