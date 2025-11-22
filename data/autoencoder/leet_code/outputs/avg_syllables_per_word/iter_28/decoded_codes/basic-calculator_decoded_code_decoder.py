from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        def helper(s: List[str]) -> int:
            stack = []
            sign = '+'
            num = 0

            while s:
                char = s.pop(0)

                if char.isdigit():
                    num = num * 10 + int(char)

                if char == '(':
                    num = helper(s)

                if (not char.isdigit() and not char.isspace()) or not s:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Python division truncates toward negative infinity
                        # The problem expects truncation toward zero
                        # So use int(a / b) instead of // for this behavior
                        stack[-1] = int(stack[-1] / num)

                    sign = char
                    num = 0

                if char == ')':
                    break

            return sum(stack)

        return helper(list(s))