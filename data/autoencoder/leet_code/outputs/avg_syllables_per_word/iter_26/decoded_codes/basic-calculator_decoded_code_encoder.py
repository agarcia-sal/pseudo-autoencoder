class Solution:
    def calculate(self, s: str) -> int:
        def helper(lst: list[str]) -> int:
            stack = []
            sign = '+'
            num = 0

            while lst:
                char = lst.pop(0)

                if char.isdigit():
                    num = num * 10 + int(char)

                if char == '(':
                    num = helper(lst)

                if (not char.isdigit() and not char.isspace()) or len(lst) == 0:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack[-1] = stack[-1] * num
                    elif sign == '/':
                        # Ensure division truncates towards zero
                        stack[-1] = int(stack[-1] / num)
                    sign = char
                    num = 0

                if char == ')':
                    break

            return sum(stack)

        return helper(list(s))