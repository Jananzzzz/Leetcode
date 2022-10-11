import math
class Solution1:          # not a good solution # need time to understand
    def increasingTriplet(self, nums: list[int]) -> bool:
        
        first, second = math.inf, math.inf
        
        for third in nums:
            
            if second < third: return [first, second, third]
            if third <= first: first= third    
            else:  second = third 
                
        return  False
test = Solution1
res = test.increasingTriplet(test, [2,1,5,0,6])
print(res)

