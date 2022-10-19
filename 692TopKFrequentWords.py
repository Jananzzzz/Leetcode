import collections
from collections import Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        m = Counter(words)
        ans = sorted(m, key = lambda x: (-m[x], x))
        return ans[:k]


words = ["calculate","i","love","leetcode","i","love","coding"]
res = Counter(words)
# sorted list by lambda function to determine the critical feature in sorting.  
ans = sorted(res, key = lambda x:(-res[x],x))
print(ans[:8])