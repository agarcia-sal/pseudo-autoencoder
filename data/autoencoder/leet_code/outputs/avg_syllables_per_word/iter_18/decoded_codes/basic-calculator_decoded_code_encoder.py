class Solution:
    def calculate(self, s: str) -> int:
        def helper(s_list) -> int:
            stack = []
            sign = '+'
            num = 0
            while s_list:
                char = s_list.pop(0)
                if char.isdigit():
                    num = num * 10 + int(char)
                if char == '(':
                    num = helper(s_list)
                if (not char.isdigit() and not char.isspace()) or not s_list:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # integer division truncating toward zero
                        val = stack[-1] / num
                        stack[-1] = int(val) if val >= 0 else int(val)
                    sign = char
                    num = 0
                if char == ')':
                    break
            return sum(stack)

        return helper(list(s))