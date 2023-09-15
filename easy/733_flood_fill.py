# https://leetcode.com/problems/flood-fill/description/

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        R, C = len(image), len(image[0])
        Color = image[sr][sc]
        if Color == color: 
            return image
        def dfs(r, c):
            if image[r][c] == Color:
                image[r][c] = color
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1) 
                if c+1 < C: dfs(r, c+1) 

        dfs(sr, sc)
        return image      
        