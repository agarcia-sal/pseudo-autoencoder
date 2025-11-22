class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    # In Python 3, int(a / b) truncates toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]