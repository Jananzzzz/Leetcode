# https://leetcode.com/problems/count-binary-substrings/description/

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        temp = []
        count = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                temp.append(count)
                count = 1
        temp.append(count)
        for i in range(len(temp)-1):
            res += min(temp[i], temp[i+1])
        return res
    
# memory efficiency 99.73%
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        temp1 = 0
        temp2 = 0
        count = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                temp1 = temp2
                temp2 = count
                if temp1 != 0:
                    res += min(temp1, temp2)
                count = 1
        temp1 = temp2
        temp2 = count
        res += min(temp1, temp2)
        return res
    
print(Solution.countBinarySubstrings(Solution(), s = "00110011"))
            