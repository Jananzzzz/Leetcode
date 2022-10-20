class Solution:
    def calculate(self, s):
        def update(op, v):
            if op == "+": stack.append(v)
            if op == "-": stack.append(-v)
            if op == "*": stack.append(stack.pop() * v)
            if op == "/": stack.append(int(stack.pop() / v))

        it, num, stack, sign = 0, 0, [], "+"


        # 3 + 2/6 - 5 
        # 3 + 2-3/6 - 5
        # 3 + 2/ (6-5)

        while it < len(s):
            if s[it].isdigit():
                num = num * 10 + int(s[it])
            elif s[it] in "+-*/":
                update(sign, num)
                num, sign = 0, s[it]
            elif s[it] == "(":
                num, j = self.calculate(s[it + 1:])
                it = it + j
            elif s[it] == ")":
                update(sign, num)
                return sum(stack), it + 1
            it += 1

        update(sign, num)
        return sum(stack)
            
# ctrl + e for move the viewport one line down
# ctrl + y for move the viewport one line up
# ctrl + u for move the viewport one page up
# ctrl + d for move the viewport one page down

# personal implementation
class MySolution:
    def calculate(self, s):
        def update(sign, v):
            if sign == "+": stack.append(v)
            if sign == "-": stack.append(-v)
            if sign == "*": stack.append(stack.pop() * v)
            if sign == "/": stack.append(int(stack.pop() / v))
    
        it, num, stack, sign = 0, 0, [], "+"

        while it < len(s):
            if s[it].isdigit():
                num = num*10 + int(s[it])
            elif s[it] in "+-*/":
                update(sign, num)
                sign, num = s[it], 0
            elif s[it] == "(":
                num, j = self.calculate(s[it+1:]) 
                it = it + j
            elif s[it] == ")":
                update(sign, num)
                return sum(stack), it + 1

            it += 1

        update(sign, num)
        return sum(stack)




# if there is spare time, implement the stack manually
# in fact, we can use list in python to roughly mimics the operation of a stack.

