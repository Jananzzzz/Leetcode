# better solution with stack:
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxlen = 0
        stack = [-1]
        for i,e in enumerate(s):
            if e == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    maxlen = max(maxlen, i - stack[-1])

        return maxlen

class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        maxlength = 0
        for i in s:
            if i == '(': left += 1
            else: right += 1

            if left < right:
                left = 0
                right = 0
                continue

            if left == right:
                #maxlength = 2*left
                maxlength = max(2*left, maxlength)
                
                
        left = 0
        right = 0

        for i in reversed(s):
            if i == ')': left += 1
            else: right += 1

            if left < right:
                left = 0
                right = 0
                continue

            if left == right:
                maxlength = max(2*left, maxlength)

        return maxlength