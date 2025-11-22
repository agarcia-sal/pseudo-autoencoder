def calculate(s):
    def helper(s_list):
        stack, sign, num = [], '+', 0
        while s_list:
            c = s_list.pop(0)
            if c.isdigit():
                num = num * 10 + int(c)
            if c == '(':
                num = helper(s_list)
            if (not c.isdigit() and c != ' ') or not s_list:
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