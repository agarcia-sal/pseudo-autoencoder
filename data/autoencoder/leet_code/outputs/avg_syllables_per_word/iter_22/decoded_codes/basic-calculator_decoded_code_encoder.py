class Solution:
    def calculate(self, s: str) -> int:
        def helper(s_list):
            stack = []
            sign = '+'
            num = 0

            while s_list:
                char = s_list.pop(0)

                if char.isdigit():
                    num = num * 10 + int(char)

                if char == '(':
                    num = helper(s_list)

                # If current char is an operator (not digit, not space) or end of list
                if (not char.isdigit() and not char.isspace()) or len(s_list) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Integer division should truncate toward zero
                        stack[-1] = int(stack[-1] / num)

                    sign = char
                    num = 0

                if char == ')':
                    break

            return sum(stack)

        return helper(list(s))