from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        def helper(s: List[str]) -> int:
            stack = []
            num = 0
            sign = '+'
            while len(s) > 0:
                char = s.pop(0)
                if char.isdigit():
                    num = num * 10 + int(char)
                if char == '(':
                    num = helper(s)
                if char in ['+', '-', '*', '/', '(', ')'] or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Truncate towards zero
                        stack[-1] = int(stack[-1] / num)
                    sign = char
                    num = 0
                if char == ')':
                    break
            return sum(stack)

        s = list(s.replace(' ', ''))
        return helper(s)