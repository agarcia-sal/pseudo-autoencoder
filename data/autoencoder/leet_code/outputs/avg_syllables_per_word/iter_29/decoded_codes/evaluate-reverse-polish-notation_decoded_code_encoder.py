class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                value_b = stack.pop()
                value_a = stack.pop()
                if token == "+":
                    stack.append(value_a + value_b)
                elif token == "-":
                    stack.append(value_a - value_b)
                elif token == "*":
                    stack.append(value_a * value_b)
                else:  # token == "/"
                    # Division that truncates towards zero
                    division_result = value_a / value_b
                    truncated_result = int(division_result) if division_result >= 0 else int(division_result)
                    # int() truncates towards zero in Python 3, so direct int() conversion suffices
                    stack.append(int(division_result))
            else:
                stack.append(int(token))
        return stack[0]