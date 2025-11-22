class Solution:
    def calculate(self, s):
        def helper(s):
            stack = []
            sign = '+'
            num = 0

            while len(s) > 0:
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
                        # Integer division truncating towards zero
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