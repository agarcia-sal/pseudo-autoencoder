class Solution:
    def calculate(self, s: str) -> int:
        def helper(s_list):
            stack = []
            number = 0
            sign = '+'
            while s_list:
                char = s_list.pop(0)
                if char.isdigit():
                    number = number * 10 + int(char)
                if char == '(':
                    number = helper(s_list)
                if char in '+-*/()' or not s_list:
                    if sign == '+':
                        stack.append(number)
                    elif sign == '-':
                        stack.append(-number)
                    elif sign == '*':
                        stack[-1] = stack[-1] * number
                    elif sign == '/':
                        # integer division truncated towards zero
                        stack[-1] = int(stack[-1] / number)
                    sign = char
                    number = 0
                if char == ')':
                    break
            return sum(stack)

        s_list = list(s)
        return helper(s_list)