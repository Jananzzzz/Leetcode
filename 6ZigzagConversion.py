class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = [[] for i in range(numRows)]
        flag = True
        # True for j go down and false for up 
        j = 0
        
        for i in s:
            if j == numRows:
                j -= 2
                flag = False
            elif j == -1:
                j += 2
                flag = True
                
            ans[j].append(i)
            
            if flag:
                j += 1
            else: 
                j -= 1
                
        res = ''
        for i in ans:
            res += ''.join(i)
            
        return res