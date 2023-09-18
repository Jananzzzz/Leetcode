# https://leetcode.com/problems/rectangle-overlap/

class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        case1 = rec1[0] in range(rec2[0]+1, rec2[2])
        case2 = rec1[2] in range(rec2[0]+1, rec2[2])
        case3 = rec2[0] in range(rec1[0]+1, rec1[2])
        case4 = rec2[2] in range(rec1[0]+1, rec1[2])
        case5 = rec1[1] in range(rec2[1]+1, rec2[3])
        case6 = rec1[3] in range(rec2[1]+1, rec2[3])
        case7 = rec2[1] in range(rec1[1]+1, rec1[3])
        case8 = rec2[3] in range(rec1[1]+1, rec1[3])
        return (case1 or case2 or case3 or case4) and (case5 or case6 or case7 or case8)

        