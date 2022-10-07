# generate all sequence consists of n characters (each character is either a or b):
'''
n = 2
def generate(A = []):
    if len(A) == n:
        ans.append("".join(A))    # A is a list, so we need to join the items in the list (convert it to a string)
        print(A)
        #ans.append(A)
        
    else:
        A.append('a')
        generate(A)
        A.pop()
        A.append('b')
        generate(A)
        A.pop()   
        
ans = []
generate()
print(ans)
'''

# method with catalan number:
# a little bit to understand

class Solution(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in  range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans

# brute force with selection:
'''
class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2*n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
'''




# brute force:
'''
class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans
'''
