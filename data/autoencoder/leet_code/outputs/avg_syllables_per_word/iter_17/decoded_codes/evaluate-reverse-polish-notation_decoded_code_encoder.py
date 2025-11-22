class Solution:
    def evalRPN(self, tokens_of_strings):
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens_of_strings:
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
                    # Python division in RPN expects truncation toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]