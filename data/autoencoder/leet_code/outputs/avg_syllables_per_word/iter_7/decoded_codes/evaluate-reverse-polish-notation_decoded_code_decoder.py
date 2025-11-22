from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: List[int] = []
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
                    # Integer division that truncates toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]