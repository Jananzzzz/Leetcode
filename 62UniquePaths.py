from calendar import c
from math import factorial
from re import A


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


# ahow will i make such stupid thinds my god.s fas A at the end of the block i  
# ahow will i make such stupid thinds my god.fasldk fasd                           # we can comment here.
# show will i make such stupid thinds my god.fa df as                              # we can comment here.
# hhow will i make such stupid thinds my god.ow can i maaf asdfasdf              we type here.   # we can comment here.
# ahow will i make such stupid thinds my god.fasdf                               we type here.   # we can comment here.
# fhow will i make such stupid thinds my god.asdjaslkd                           we type here.   # we can comment here.
# vhow will i make such stupid thinds my god.                                    we type here.   # we can comment here.


# vhow will i make such stupid thinds my mmm.                                    we type here.   # we can comment here.
# vhow will i make such stupid thinds my mmm.                                    we type here.   # we can comment here.
# vhow will i make such stupid thinds my mmm.                                    we type here.   # we can comment here.
# you can use "r" to replace the selected can i ffff.
# awesome

