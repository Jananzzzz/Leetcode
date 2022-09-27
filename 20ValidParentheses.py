class Solution:
    def isValid(self, s: str) -> bool:
        
        pair = {
        '(': ')',
        '[': ']',
        '{': '}'
        }
        open = {'(', '[', '{'}
        stack = []
        for charac in s:
            if charac in open:
                stack.append(charac)
            else:
                if len(stack) and pair[stack[-1]] == charac:
                    stack.pop()
                else:
                    return False
        if len(stack):
            return False
        return True