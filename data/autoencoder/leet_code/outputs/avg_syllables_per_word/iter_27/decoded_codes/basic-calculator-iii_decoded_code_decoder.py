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

                # Evaluate if current char is an operator or ')' or end of expression
                if (char in '+-*/' or char == ')' or not s_list):
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Truncate towards zero
                        top = stack[-1]
                        if top // num < 0 and top % num != 0:
                            stack[-1] = top // num + 1
                        else:
                            stack[-1] = top // num

                    if char == ')':
                        break

                    sign = char
                    num = 0

            return sum(stack)

        s_list = list(s)
        return helper(s_list)