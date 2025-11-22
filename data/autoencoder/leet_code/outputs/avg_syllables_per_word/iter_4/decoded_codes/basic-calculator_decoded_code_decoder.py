class Solution:
    def calculate(self, s: str) -> int:
        def helper(s_list: list) -> int:
            stack = []
            sign = '+'
            num = 0

            while s_list:
                char = s_list.pop(0)

                if char.isdigit():
                    num = num * 10 + int(char)

                elif char == '(':
                    num = helper(s_list)

                if (not char.isdigit() and not char.isspace()) or not s_list:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Use int() to truncate towards zero as in original C++/Java behavior
                        stack[-1] = int(stack[-1] / num)
                    sign = char
                    num = 0

                if char == ')':
                    break

            return sum(stack)

        return helper(list(s))