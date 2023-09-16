# https://leetcode.com/problems/largest-triangle-area/

class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        area = 0
        for i in range(len(points)-2):
            for j in range(i, len(points)-1):
                for k in range(j, len(points)):
                    vect_a = [points[k][0]-points[i][0], points[k][1]-points[i][1]]
                    vect_b = [points[j][0]-points[i][0], points[j][1]-points[i][1]]
                    area = max(area, 1/2 * abs(vect_a[0]*vect_b[1]-vect_a[1]*vect_b[0]))
        return area
    
