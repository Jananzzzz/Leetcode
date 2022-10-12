class Solution1:
    def largestMerge(self,s1:str,s2:str) -> str:
        if s1 >= s2 > "":
            return s1[0] + self.largestMerge(self,s1[1:],s2)
        if s2 >= s1 > "":
            return s2[0] + self.largestMerge(self,s1,s2[1:])
        return s1 + s2  # if any one of string1 and string 2 is empty, return the other one.

class Solution2:
    def largestMerge(self,s1:str,s2:str) -> str:
        ans = ""
        while s1 and s2:
            if s1 >= s2:
                ans += s1[0]
                s1 = s1[1:]
            else:
                ans += s2[0]
                s2 = s2[1:]
        ans += s1
        ans += s2
        return ans

test = Solution2
res = test.largestMerge(test,"abs","c")
print(res)
