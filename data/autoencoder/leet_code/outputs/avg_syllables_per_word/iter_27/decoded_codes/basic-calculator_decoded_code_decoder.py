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
                        # Implement integer division truncating towards zero
                        dividend = stack[-1]
                        divisor = num
                        if dividend * divisor < 0:
                            stack[-1] = -(-dividend // divisor)
                        else:
                            stack[-1] = dividend // divisor
                    sign = char
                    num = 0
                if char == ')':
                    break
            return sum(stack)
        return helper(list(s))