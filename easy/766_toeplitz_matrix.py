# https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                try:
                    if matrix[i][j] != matrix[i+1][j+1]:
                        return False
                except:
                    pass
        return True

        
        