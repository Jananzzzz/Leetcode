'''
x = 123
print(str(x))
y = str(x)
print(type(y))
print(y[2])
'''

'''# solution with string 
class Solution:
    def isPalindrome(self, x: int) -> bool:     
        y = str(x)   
        for i in range(int(len(y)/2)):
            if y[i] == y[-i-1]:
                continue
            else:
                return False
        return True
'''

# solution without using string  space is O(1)                

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        if x == 0 : return True
        revert = 0
        while(revert < x): 
            revert = revert*10 + x%10
            x /= 10
        print(x, revert)
        return x == revert or x == revert/10

test = Solution()
# test.isPalindrome(int(input("enter your integer")))
test.isPalindrome(1)





















