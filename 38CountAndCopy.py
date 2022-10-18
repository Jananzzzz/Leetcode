# from top to the bottom (n -> 1)
class Solution0:       
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        if n == 2: return "11"
        res = ""
        count = 1
        dummy = self.countAndSay(self,n-1)
        for i in range(len(dummy)-1):
            if dummy[i] == dummy[i+1]:
                count += 1
                if i == len(dummy)-2:
                    res = res + str(count) + dummy[i]
            else:
                res = res + str(count) + dummy[i]
                count = 1
        if len(dummy)>=2:
            if dummy[-1] != dummy[-2]:
                res = res + "1" + dummy[-1]
        return res 


# from bottom to the top
class Solution1:
    def countAndSay(n):
        s = '1'
        for _ in range(n-1):
            let, temp, count = s[0], '', 0
            for i in s:
                if let == i:
                    count += 1
                else:
                    temp += str(count) + let
                    let = i
                    count = 1
            temp += str(count) + let
            s = temp
        return s

# from bottom to the top:
# more efficient to use ".join()" to concatenate strings.
class Solution2:
    def countAndSay(n):
        s = '1'
        for i in range(n-1):
            count = 1
            temp = []
            for index in range(1, len(s)):
                if s[index] == s[index-1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(s[index-1])
                    count = 1
            temp.append(str(count))
            temp.append(s[-1])
            s = ''.join(temp)
        return s


test = Solution2
res = test.countAndSay(4)
print(res)
