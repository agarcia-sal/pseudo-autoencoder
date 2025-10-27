class Solution:
    def evalRPN(self, tokens):
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                else:  # token == "/"
                    # int() truncates towards zero in Python 3
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]