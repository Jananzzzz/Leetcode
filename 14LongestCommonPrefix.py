class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ListLength = []

        for i in range(len(strs)):
            ListLength.append(len(strs[i]))
        ListLength.sort()
        min = ListLength[0]
        output = ""

        for i in range(min):
            LengthSum = 0
            for j in range(len(strs)):
                if strs[j][i] == strs[0][i]:
                    LengthSum += 1
                else:
                    break
            if LengthSum == len(strs):
                output = output + strs[0][i] 
            else:
                break

        return(output)
        