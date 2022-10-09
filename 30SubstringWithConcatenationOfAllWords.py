

# brute force (sometimes time exceeded limit)
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
    
        res = []

        k1 = len(words[0])
        k2 = k1 * len(words)
        #print(k1)
        #print(k2)

        def checkPermmuation(string, x:int):
            #print(dummy)
            for i in range(len(string)):
                if i%k1 == 0:
                    if string[i:i+k1] in dummy:
                        dummy.remove(string[i:i+k1])
            if dummy == []:
                res.append(x)

        for i in range(len(s)-k2+1):
            string = s[i:i+k2]
            x = i
            dummy = words[:]
            checkPermmuation(string, x)
            
            
        print(words)

        return res
'''