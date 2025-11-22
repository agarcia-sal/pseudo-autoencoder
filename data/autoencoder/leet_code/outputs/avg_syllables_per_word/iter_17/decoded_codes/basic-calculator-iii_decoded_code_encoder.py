class Solution:
    def calculate(self, string_s: str) -> int:
        def helper(list_s: list) -> int:
            stack = []
            num = 0
            sign = '+'

            while len(list_s) > 0:
                char = list_s.pop(0)

                if char.isdigit():
                    num = num * 10 + int(char)

                if char == '(':
                    num = helper(list_s)

                if char in '+-*/()' or len(list_s) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Integer division truncating towards zero
                        stack[-1] = int(stack[-1] / num)
                    sign = char
                    num = 0

                if char == ')':
                    break

            return sum(stack)

        return helper(list(string_s))