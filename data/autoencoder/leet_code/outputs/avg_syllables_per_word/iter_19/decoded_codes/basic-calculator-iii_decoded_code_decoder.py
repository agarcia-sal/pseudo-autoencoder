class Solution:
    def calculate(self, s):
        def helper(s):
            stack = []
            num = 0
            sign = '+'
            while s:
                char = s.pop(0)
                if char.isdigit():
                    num = num * 10 + int(char)
                if char == '(':
                    num = helper(s)
                # If char is operator, parenthesis, or s is empty, process the previous sign and num
                if char in '+-*/()' or not s:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # truncate towards zero
                        stack[-1] = int(stack[-1] / num)
                    sign = char
                    num = 0
                if char == ')':
                    break
            return sum(stack)

        s = list(s)
        return helper(s)