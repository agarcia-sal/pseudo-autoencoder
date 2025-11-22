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
                    # Python int division truncates towards negative infinity,
                    # but RPN division truncates towards zero.
                    # Use int(a / b) to truncate towards zero.
                    # Also handle division by zero just in case.
                    if b == 0:
                        raise ZeroDivisionError("division by zero in evalRPN")
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]