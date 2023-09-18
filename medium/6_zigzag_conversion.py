# https://leetcode.com/problems/zigzag-conversion/description/

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# P   A   H   N
# A P L S I I G
# Y   I   R


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for i in range(numRows)]
        zags = len(s) // (2 * (numRows - 1)) + 2
        for i in range(len(rows)):
            for j in range(zags):
                try:
                    if i != 0 and i != len(rows) - 1:
                        if j * (2*(numRows-1)) - i >= 0:
                            rows[i].append(s[j * (2*(numRows-1)) - i])
                        rows[i].append(s[j * (2*(numRows-1)) + i])
                    elif i == len(rows) - 1:
                        rows[i].append(s[j * (2*(numRows-1)) + i])
                    else:
                        rows[i].append(s[j * (2*(numRows-1))])
                except:
                    pass
        res_list = []
        for i in rows:
            res_list.extend(i)
        res = ''.join(res_list)
        return res

print(Solution.convert(Solution(), s = "PAYPALISHIRING", numRows = 3))
print(Solution.convert(Solution(), s = "ABCDE", numRows = 4))
