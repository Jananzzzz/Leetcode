"""
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            result += chr(ord("A") + (columnNumber - 1) % 26)
            columnNumber = (columnNumber - 1) // 26
        return result