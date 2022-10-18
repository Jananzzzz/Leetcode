class Solution:
    def maxLength(A: list[str]):
        dp = [set()]
        for a in A:
            if len(set(a)) < len(a): continue  # duplicated characters in a 
            a = set(a)      # set("abbs") == {"a", "b", "s"}
            for c in dp[:]:
                if a & c: continue
                dp.append(a | c)
        return max(len(a) for a in dp)

test = Solution
res = test.maxLength(["cha","r","act","ers"])
print(res)
class Solution1:
    def maxLength(A: list[str]):
        dp = [set()]
        for a in A:
            if len(set(a)) < len(a): continue
            a = set(a)
            for c in dp[:]:
                if a & c: continue
                dp.append(a | c)
        return max(len(a) for a in dp)