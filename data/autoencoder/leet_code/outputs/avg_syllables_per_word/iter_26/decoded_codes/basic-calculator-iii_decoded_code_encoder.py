class Solution:
    def calculate(self, s: str) -> int:
        def helper(lst: list) -> int:
            stack = []
            number = 0
            sign = '+'
            while lst:
                ch = lst.pop(0)
                if ch.isdigit():
                    number = number * 10 + int(ch)
                if ch == '(':
                    number = helper(lst)
                if ch in '+-*/()' or not lst:
                    if sign == '+':
                        stack.append(number)
                    elif sign == '-':
                        stack.append(-number)
                    elif sign == '*':
                        stack[-1] = stack[-1] * number
                    elif sign == '/':
                        # truncate towards zero
                        top = stack[-1]
                        if top // number < 0 and top % number != 0:
                            stack[-1] = top // number + 1
                        else:
                            stack[-1] = top // number
                    sign = ch
                    number = 0
                if ch == ')':
                    break
            return sum(stack)

        return helper(list(s))