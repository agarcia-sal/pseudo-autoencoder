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
                    # Python division truncates towards -inf, need to truncate towards zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]