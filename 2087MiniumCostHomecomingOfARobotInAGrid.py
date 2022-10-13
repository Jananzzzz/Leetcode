class Solution:
    def minCost(self, startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:
        def cmp(a, b):
            return (a>b) - (a<b)
    
        res, [i, j], [x, y] = 0, startPos, homePos
        while i != x:
            i += cmp(x, i)
            res += rowCosts[i]
        while j != y:
            j += cmp(y, j)
            res += colCosts[j]
        return res


        # replace all the occurence in a line
        # :s/old/new/g
        # without "g", only change the first occurrence.