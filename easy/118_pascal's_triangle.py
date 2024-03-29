"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
"""

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = [[1]]
        prev = [1]
        count = 1
        while(count < numRows):
            new = []
            new.append(prev[0])
            for i in range(len(prev)-1):
                new.append(prev[i] + prev[i+1])
            new.append(prev[-1])
            res.append(new)
            prev = new
            count += 1
        return res

print(Solution.generate(Solution(), 5))
print(Solution.generate(Solution(), 1))
            
            