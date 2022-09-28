class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        kong = False
        counter = 0
        for i in s:
            if kong and i != " ":
                counter = 0
            if i == " ":
                kong = True
            else: 
                kong = False
                counter += 1
        return counter