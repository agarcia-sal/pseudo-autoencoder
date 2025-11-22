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

                if (not char.isdigit() and not char.isspace()) or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Python division truncates towards negative infinity,
                        # but the problem expects truncation towards zero
                        # so we use int() on float division to truncate towards zero
                        stack[-1] = int(stack[-1] / num)

                    sign = char
                    num = 0

                if char == ')':
                    break

            return sum(stack)

        # Convert string s into a list of characters for easy manipulation
        return helper(list(s))