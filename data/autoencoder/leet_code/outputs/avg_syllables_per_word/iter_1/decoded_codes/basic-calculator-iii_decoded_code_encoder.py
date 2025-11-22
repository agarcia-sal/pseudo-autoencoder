def calculate(s):
    def helper(s):
        stack, num, sign = [], 0, '+'
        while s:
            c = s.pop(0)
            if c.isdigit():
                num = num * 10 + int(c)
            if c == '(':
                num = helper(s)
            if c in '+-*/()' or not s:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                elif sign == '/':
                    stack[-1] = int(stack[-1] / num)
                sign = c
                num = 0
            if c == ')':
                break
        return sum(stack)
    return helper(list(s))