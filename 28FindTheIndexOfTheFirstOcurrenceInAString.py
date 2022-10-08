# input: "sadbutsad", "sad"
# output: 0

# KMP algorithm

# brute force

def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i: i+len(needle)] == needle:
            return i
    return -1

res = strStr("butsad", "sad")
print(res)


# python built-in string map:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return(haystack.index(needle))
        except:
            return(-1)

