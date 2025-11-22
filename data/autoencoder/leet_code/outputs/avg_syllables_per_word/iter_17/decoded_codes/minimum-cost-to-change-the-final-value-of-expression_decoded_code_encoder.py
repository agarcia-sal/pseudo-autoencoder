class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        stack = []
        for el in expression:
            if el in ('(', '&', '|'):
                stack.append((el, 0))
                continue

            if el == ')':
                lastPair = stack.pop()
                stack.pop()  # remove the opening parenthesis
            else:
                lastPair = (int(el), 1)  # el is '0' or '1'

            if stack and stack[-1][0] in ('&', '|'):
                op = stack.pop()[0]
                a, costA = stack.pop()
                b, costB = lastPair

                if op == '&':
                    # Evaluate AND logic for flip cost and value
                    if a == 0 and b == 0:
                        lastPair = (0, 1 + min(costA, costB))
                    elif (a == 0 and b == 1) or (a == 1 and b == 0):
                        lastPair = (0, 1)
                    else:  # a == 1 and b == 1
                        lastPair = (1, min(costA, costB))
                else:  # op == '|'
                    # Evaluate OR logic for flip cost and value
                    if a == 0 and b == 0:
                        lastPair = (0, min(costA, costB))
                    elif (a == 0 and b == 1) or (a == 1 and b == 0):
                        lastPair = (1, 1)
                    else:  # a == 1 and b == 1
                        lastPair = (1, 1 + min(costA, costB))

            stack.append(lastPair)

        return stack[-1][1]