class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # a more simple code with same method
        count = -1
        a = dividend
        b = divisor
        dividend = abs(dividend)
        divisor = abs(divisor)
        adder = 1
        
        # computing core:
        while dividend >= 0:
            if dividend >= divisor:
                dividend -= divisor
                count += adder
                adder += adder
                divisor += divisor 

            if dividend < divisor:
                divisor = abs(b)
                dividend -= divisor
                adder = 1
                count += adder
            
            
        if (a>=0 and b>0) or (a<=0 and b<0):
            if count > 2**31 -1:
                return 2**31 - 1
            else: return count
        else: 
            if count < -2**31:
                return -2**32
            else: return -count
     
        
        
'''
count       -1     0    2     6      14     30
dividend     200  196   188   172   150    86    
divisor     4       8    16    32    64    128   4
adder       1      2    4       8    16    32
'''

