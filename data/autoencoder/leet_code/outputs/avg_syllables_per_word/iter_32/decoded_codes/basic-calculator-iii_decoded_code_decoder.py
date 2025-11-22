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

                # If char is an operator or right parenthesis or end of list,
                # process the stack with the current sign and num
                if (
                    char in '+-*/)' or
                    len(s_list) == 0
                ):

                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Division truncated towards zero
                        top = stack[-1]
                        if top < 0:
                            stack[-1] = - (abs(top) // num)
                        else:
                            stack[-1] = top // num

                    sign = char
                    num = 0

                if char == ')':
                    break

            return sum(stack)

        s_list = list(s.replace(' ', ''))
        return helper(s_list)