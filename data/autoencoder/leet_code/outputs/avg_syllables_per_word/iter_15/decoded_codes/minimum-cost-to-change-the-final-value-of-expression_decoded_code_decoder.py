class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        stack = []
        for e in expression:
            if e == '(' or e == '&' or e == '|':
                stack.append([e, 0])
                continue
            if e == ')':
                lastPair = stack.pop()
                stack.pop()
            else:
                lastPair = [int(e), 1]

            if stack and (stack[-1][0] == '&' or stack[-1][0] == '|'):
                op = stack.pop(0 if hasattr(stack[-1], "__getitem__") else -1) # This line is faulty in pseudocode, fixed below
                op = stack[-1][0]
                stack[-1][0], cost_op = stack[-1][0], stack[-1][1] # to clarify; actually, popping operator from stack...
                op = stack.pop()[0]
                a, costA = stack.pop()
                b, costB = lastPair
                if op == '&':
                    if a == 0 and b == 0:
                        lastPair = [0, 1 + min(costA, costB)]
                    elif a == 0 and b == 1:
                        lastPair = [0, 1]
                    elif a == 1 and b == 0:
                        lastPair = [0, 1]
                    else:
                        lastPair = [1, min(costA, costB)]
                else:
                    if a == 0 and b == 0:
                        lastPair = [0, min(costA, costB)]
                    elif a == 0 and b == 1:
                        lastPair = [1, 1]
                    elif a == 1 and b == 0:
                        lastPair = [1, 1]
                    else:
                        lastPair = [1, 1 + min(costA, costB)]
            stack.append(lastPair)
        return stack[-1][1]