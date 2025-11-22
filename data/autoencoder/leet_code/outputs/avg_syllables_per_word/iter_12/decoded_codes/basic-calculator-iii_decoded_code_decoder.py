class Solution:
    def calculate(self, s: str) -> int:
        def helper(s_list):
            stack = []
            num = 0
            sign = '+'
            while len(s_list) > 0:
                char = s_list.pop(0)
                if char.isdigit():
                    num = num * 10 + int(char)
                if char == '(':
                    num = helper(s_list)
                if char in '+-*/()' or len(s_list) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # truncate towards zero for division
                        last = stack[-1]
                        if last < 0:
                            stack[-1] = -(-last // num)
                        else:
                            stack[-1] = last // num
                    sign = char
                    num = 0
                if char == ')':
                    break
            return sum(stack)

        return helper(list(s))