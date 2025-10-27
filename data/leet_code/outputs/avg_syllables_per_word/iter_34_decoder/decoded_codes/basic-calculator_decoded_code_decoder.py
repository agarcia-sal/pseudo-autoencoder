class Solution:
    def calculate(self, s: str) -> int:
        def helper(s: list) -> int:
            stack = []
            sign = '+'
            num = 0
            while len(s) > 0:
                char = s.pop(0)
                if char.isdigit():
                    num = num * 10 + int(char)
                if char == '(':
                    num = helper(s)
                # Process when current char is an operator or end of input
                if (not char.isdigit() and not char.isspace()) or len(s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Python division truncates towards negative infinity, use int(...) to truncate towards zero
                        stack[-1] = int(stack[-1] / num)
                    sign = char
                    num = 0
                if char == ')':
                    break
            return sum(stack)
        return helper(list(s))