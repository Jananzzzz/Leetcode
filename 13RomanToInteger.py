class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        for i in range (len(s)-1):
            if s[i] == 'M':
                sum += 1000
            if s[i] == 'D':
                sum += 500
            if s[i] == 'C':
                sum += 100
                if s[i+1] == 'D':
                    sum -= 200
                if s[i+1] == 'M':
                    sum -= 200
            if s[i] == 'L':
                sum += 50
            if s[i] == 'X':
                sum += 10
                if s[i+1] == 'L':
                    sum -= 20
                if s[i+1] == 'C':
                    sum -= 20
            if s[i] == 'V':
                sum += 5
            if s[i] == 'I':
                sum +=1	
                if s[i+1] == 'V':
                    sum -= 2
                if s[i+1] == 'X':
                    sum -= 2
        if s[len(s)-1] == 'M': sum += 1000
        if s[len(s)-1] == 'D': sum += 500
        if s[len(s)-1] == 'C': sum += 100
        if s[len(s)-1] == 'L': sum += 50
        if s[len(s)-1] == 'X': sum += 10
        if s[len(s)-1] == 'V': sum += 5
        if s[len(s)-1] == 'I': sum += 1
        return sum