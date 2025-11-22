from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        def helper(s_list: List[str]) -> int:
            stack: List[int] = []
            num = 0
            sign = '+'
            while len(s_list) > 0:
                char = s_list.pop(0)
                if char.isdigit():
                    num = num * 10 + int(char)
                if char == '(':
                    num = helper(s_list)
                if (char in '+-*/()') or len(s_list) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Integer division truncating towards zero:
                        top = stack[-1]
                        if top // num < 0 and top % num != 0:
                            stack[-1] = top // num + 1
                        else:
                            stack[-1] = top // num
                    sign = char
                    num = 0
                if char == ')':
                    break
            return sum(stack)
        s_list = list(filter(lambda ch: ch != ' ', s))
        return helper(s_list)