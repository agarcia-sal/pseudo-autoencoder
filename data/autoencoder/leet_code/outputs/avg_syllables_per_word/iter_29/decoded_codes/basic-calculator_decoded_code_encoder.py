class Solution:
    def calculate(self, s: str) -> int:
        def helper(s_list):
            stack = []
            sign = '+'
            number = 0

            while s_list:
                char = s_list.pop(0)

                if char.isdigit():
                    number = number * 10 + int(char)

                if char == '(':
                    number = helper(s_list)

                if (not char.isdigit() and not char.isspace()) or len(s_list) == 0:
                    if sign == '+':
                        stack.append(number)
                    elif sign == '-':
                        stack.append(-number)
                    elif sign == '*':
                        stack[-1] = stack[-1] * number
                    elif sign == '/':
                        # Perform integer division truncating towards zero
                        stack[-1] = int(stack[-1] / number)

                    sign = char
                    number = 0

                if char == ')':
                    break

            return sum(stack)

        return helper(list(s))