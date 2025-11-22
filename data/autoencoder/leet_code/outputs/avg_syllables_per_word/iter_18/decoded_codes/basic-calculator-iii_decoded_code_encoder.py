class Solution:
    def calculate(self, s: str) -> int:
        def helper(s: list) -> int:
            stack = []
            num = 0
            sign = '+'
            while s:
                char = s.pop(0)
                if char.isdigit():
                    num = num * 10 + int(char)
                if char == '(':
                    num = helper(s)
                if char in '+-*/()' or not s:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Integer division with truncation towards zero
                        stack[-1] = int(stack[-1] / num)
                    sign = char
                    num = 0
                if char == ')':
                    break
            return sum(stack)
        s = list(s.replace(' ', ''))
        return helper(s)