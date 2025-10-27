class Solution:
    def calculate(self, s: str) -> int:
        def helper(s_list):
            stack = []
            sign = '+'
            num = 0

            while len(s_list) > 0:
                char = s_list.pop(0)

                if char.isdigit():
                    num = num * 10 + int(char)

                if char == '(':
                    num = helper(s_list)

                # If char is an operator or closing parenthesis or end of string
                if (not char.isdigit() and not char.isspace()) or len(s_list) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Integer division that truncates towards zero
                        stack[-1] = int(stack[-1] / num)

                    sign = char
                    num = 0

                if char == ')':
                    break

            return sum(stack)

        return helper(list(s))