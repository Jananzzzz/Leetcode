def lengthOfLongestSubstring(self, s: str) -> int:
    tmp, length = "", 0
    for i in range(len(s)):
        if s[i] in tmp:
            length = max(len(tmp),length)
            ind = tmp.index(s[i])
            tmp = tmp[ind+1:]

        tmp += s[i]            
    return max(len(tmp),length)
