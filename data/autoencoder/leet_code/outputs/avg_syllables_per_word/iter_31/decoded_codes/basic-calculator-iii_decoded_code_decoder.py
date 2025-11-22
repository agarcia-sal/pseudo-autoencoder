from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        def helper(s_list: List[str]) -> int:
            stack = []
            num = 0
            sign = '+'

            while s_list:
                char = s_list.pop(0)

                if char.isdigit():
                    num = num * 10 + int(char)

                if char == '(':
                    num = helper(s_list)

                if (char in '+-*/' or char == ')' or not s_list):
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Division truncates toward zero
                        top = stack[-1]
                        result = int(top / num)
                        stack[-1] = result
                    sign = char
                    num = 0

                if char == ')':
                    break

            return sum(stack)

        return helper(list(s))