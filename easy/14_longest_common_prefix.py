"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        index = 0
        for i in range(201):
            try:
                count = 0
                for j in range(len(strs)):
                    if strs[j][i] == strs[0][i]:
                        count += 1
                if count == len(strs):
                    index += 1
                else:
                    return strs[0][:index]
            except:
                return strs[0][:index]
    
print(Solution.longestCommonPrefix(Solution(), strs=["dog","racecar","car"]))
print(Solution.longestCommonPrefix(Solution(), strs=["flower","flow","flight"]))


        
