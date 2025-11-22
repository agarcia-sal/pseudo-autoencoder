from typing import List, Tuple

class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        stack: List[Tuple[int, int]] = []
        for e in expression:
            if e in ('(', '&', '|'):
                stack.append((e, 0))
                continue
            elif e == ')':
                last_pair = stack.pop()
            else:
                last_pair = (int(e), 1)

            if stack and stack[-1][0] in ('&', '|'):
                op = stack.pop()[0]
                a, costA = stack.pop()
                b, costB = last_pair
                if op == '&':
                    if a == 0 and b == 0:
                        last_pair = (0, 1 + min(costA, costB))
                    elif (a == 0 and b == 1) or (a == 1 and b == 0):
                        last_pair = (0, 1)
                    else:  # a == 1 and b == 1
                        last_pair = (1, min(costA, costB))
                else:  # op == '|'
                    if a == 0 and b == 0:
                        last_pair = (0, min(costA, costB))
                    elif (a == 0 and b == 1) or (a == 1 and b == 0):
                        last_pair = (1, 1)
                    else:  # a == 1 and b == 1
                        last_pair = (1, 1 + min(costA, costB))
            stack.append(last_pair)
        return stack[-1][1]