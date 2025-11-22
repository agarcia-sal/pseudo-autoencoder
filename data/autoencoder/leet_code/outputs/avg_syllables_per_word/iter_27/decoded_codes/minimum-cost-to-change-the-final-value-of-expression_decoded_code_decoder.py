class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        stack = []

        for e in expression:
            if e == '(' or e == '&' or e == '|':
                stack.append((e, 0))
                continue
            elif e == ')':
                # Pop the last element (value, cost) within the parentheses
                lastPair = stack.pop()
                # Pop the opening '(' which should be before lastPair
                stack.pop()
            else:
                # e is '0' or '1'
                lastPair = (e, 1)

            if stack and (stack[-1][0] == '&' or stack[-1][0] == '|'):
                op = stack.pop()[0]
                a, costA = stack.pop()
                b, costB = lastPair

                if op == '&':
                    if a == '0' and b == '0':
                        lastPair = ('0', 1 + min(costA, costB))
                    elif a == '0' and b == '1':
                        lastPair = ('0', 1)
                    elif a == '1' and b == '0':
                        lastPair = ('0', 1)
                    else:  # a == '1' and b == '1'
                        lastPair = ('1', min(costA, costB))
                else:  # op == '|'
                    if a == '0' and b == '0':
                        lastPair = ('0', min(costA, costB))
                    elif a == '0' and b == '1':
                        lastPair = ('1', 1)
                    elif a == '1' and b == '0':
                        lastPair = ('1', 1)
                    else:  # a == '1' and b == '1'
                        lastPair = ('1', 1 + min(costA, costB))

            stack.append(lastPair)

        return stack[-1][1] if stack else 0