# https://leetcode.com/problems/baseball-game/description/

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        res = []
        for i in operations:
            if i == "+":
                res.append(res[-1]+res[-2])
            elif i == "D":
                res.append(res[-1]*2)
            elif i == "C":
                res.pop()
            else: 
                res.append(int(i))
        return sum(res)
    
print(Solution.calPoints(Solution(), ["5","2","C","D","+"]))