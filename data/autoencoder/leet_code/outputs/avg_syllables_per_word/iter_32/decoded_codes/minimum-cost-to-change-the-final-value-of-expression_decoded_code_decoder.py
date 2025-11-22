from typing import List, Tuple

class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        stack: List[Tuple[int, int]] = []
        # Use int 0/1 instead of '0'/'1' for clarity

        for e in expression:
            if e in ('(', '&', '|'):
                # push (operator or '(' , cost 0)
                stack.append((e, 0))
                continue

            if e == ')':
                # pop last element as lastPair
                lastPair = stack.pop()
            else:
                # operand character '0' or '1'
                lastPair = (int(e), 1)

            # check if top of stack is operator & or |
            while stack and stack[-1][0] in ('&', '|'):
                op, _ = stack.pop()
                a, costA = stack.pop()
                b, costB = lastPair

                if op == '&':
                    if a == 0 and b == 0:
                        # AND(0,0) == 0; to flip result requires 1 + min(costA,costB)
                        lastPair = (0, 1 + min(costA, costB))
                    elif a == 0 and b == 1:
                        # AND(0,1) == 0; to flip result requires 1 op change only (so cost=1)
                        lastPair = (0, 1)
                    elif a == 1 and b == 0:
                        # AND(1,0) == 0; same as above
                        lastPair = (0, 1)
                    else:
                        # AND(1,1) == 1; to flip result requires min(costA,costB)
                        lastPair = (1, min(costA, costB))

                else:  # op == '|'
                    if a == 0 and b == 0:
                        # OR(0,0) == 0; to flip result requires min(costA, costB)
                        lastPair = (0, min(costA, costB))
                    elif a == 0 and b == 1:
                        # OR(0,1) == 1; flip requires 1 (flip op only)
                        lastPair = (1, 1)
                    elif a == 1 and b == 0:
                        # OR(1,0) == 1; flip requires 1
                        lastPair = (1, 1)
                    else:
                        # OR(1,1) == 1; flip requires 1 + min(costA, costB)
                        lastPair = (1, 1 + min(costA, costB))

            stack.append(lastPair)

        # result cost is second element of lastPair in stack
        return stack[-1][1] if stack else 0