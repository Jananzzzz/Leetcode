"""
https://leetcode.com/problems/pascals-triangle-ii/
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
"""

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        prev = [1]
        count = 0
        while(count < rowIndex):
            new = []
            new.append(prev[0])
            for i in range(len(prev)-1):
                new.append(prev[i] + prev[i+1])
            new.append(prev[-1])
            prev = new
            count += 1
        return prev

print(Solution.getRow(Solution(), 3))