class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        new_string = ""
        
        if len(s) == 0:
            return 0
        elif not s[0].isnumeric() and (s[0] != "-" and s[0] != "+"):
            return 0
        else:
            if s[0] == "-":
                sign = -1
            else:
                sign = 1
            #sign = -1 if s[0]="-" else 1
            
            if s[0] == "-" or s[0] == "+":
                s = s[1:]
            
            '''
            for i in range(len(s)):
                if s[i].isnumeric():
                    for j in range(i, len(s)):
                        if s[j].isnumeric():
                            new_string += s[j]
                        else: break
                    break
            '''
            
            for i in s:
                if i.isnumeric():
                    new_string += i
                else: break
                    
            if new_string == "":
                return 0
                
            
            num = int(new_string) if sign == 1 else (- int(new_string))

            if num > 2**31-1: return 2**31-1
            if num < -2**31:  return -2**31

            return num
        
        