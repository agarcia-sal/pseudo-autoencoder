class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # token == "/"
                    # Perform division truncating toward zero
                    division_result = a / b
                    truncated_result = int(division_result) if division_result >= 0 else int(division_result)
                    # int() in Python already truncates toward zero, but to be explicit:
                    truncated_result = int(division_result)
                    stack.append(truncated_result)
            else:
                stack.append(int(token))
        return stack[0]