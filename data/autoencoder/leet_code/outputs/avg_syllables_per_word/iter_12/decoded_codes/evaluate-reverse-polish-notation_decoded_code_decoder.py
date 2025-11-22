import math
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
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
                    result = a / b
                    if result >= 0:
                        result = math.floor(result)
                    else:
                        result = math.ceil(result)
                    stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]