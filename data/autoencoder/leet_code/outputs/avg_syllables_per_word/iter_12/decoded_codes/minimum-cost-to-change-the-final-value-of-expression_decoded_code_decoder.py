class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        stack = []

        for e in expression:
            if e == '(' or e == '&' or e == '|':
                stack.append([e, 0])
                continue

            if e == ')':
                # Pop last pair inside the parentheses
                lastPair = stack.pop()
                # Pop the '('
                stack.pop()
            else:
                # e is '0' or '1'
                lastPair = [int(e), 1]

            # Check if stack top is operator & or |
            while stack and (stack[-1][0] == '&' or stack[-1][0] == '|'):
                op = stack.pop()[0]
                a, costA = stack.pop()
                b, costB = lastPair

                if op == '&':
                    if a == 0 and b == 0:
                        # Both zero: result 0, cost 1 + min costs to flip one
                        lastPair = [0, 1 + min(costA, costB)]
                    elif (a == 0 and b == 1) or (a == 1 and b == 0):
                        # One zero and one one: result 0, cost 1
                        lastPair = [0, 1]
                    else:
                        # Both one: result 1, cost min costs to flip one
                        lastPair = [1, min(costA, costB)]
                else:  # op == '|'
                    if a == 0 and b == 0:
                        # both zero: result 0, cost min costs to flip one
                        lastPair = [0, min(costA, costB)]
                    elif (a == 0 and b == 1) or (a == 1 and b == 0):
                        # one zero one one: result 1, cost 1
                        lastPair = [1, 1]
                    else:
                        # both one: result 1, cost 1 + min costs to flip one
                        lastPair = [1, 1 + min(costA, costB)]

            stack.append(lastPair)

        return stack[-1][1]