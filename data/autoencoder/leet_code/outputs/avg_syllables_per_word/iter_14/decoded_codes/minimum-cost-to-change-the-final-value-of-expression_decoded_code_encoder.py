class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        stack = []

        for e in expression:
            if e in ('(', '&', '|'):
                stack.append([e, 0])
                continue

            if e == ')':
                lastPair = stack.pop()
                stack.pop()  # discard the opening parenthesis
            else:
                # e is '0' or '1'
                lastPair = [e, 1]  # cost to flip '0'->'1' or '1'->'0' is 1

            if stack and stack[-1][0] in ('&', '|'):
                op = stack.pop()[0]
                a, costA = stack.pop()
                b, costB = lastPair

                if op == '&':
                    if a == '0' and b == '0':
                        # Change & to | and OR result to '1'
                        lastPair = ['0', 1 + min(costA, costB)]
                    elif (a == '0' and b == '1') or (a == '1' and b == '0'):
                        # Change & to |
                        lastPair = ['0', 1]
                    else:  # a == '1' and b == '1'
                        # Change OR result to '0'
                        lastPair = ['1', min(costA, costB)]
                else:  # op == '|'
                    if a == '0' and b == '0':
                        # Change OR result to '1'
                        lastPair = ['0', min(costA, costB)]
                    elif (a == '0' and b == '1') or (a == '1' and b == '0'):
                        # Change | to &
                        lastPair = ['1', 1]
                    else:  # a == '1' and b == '1'
                        # Change | to & and OR result to '0'
                        lastPair = ['1', 1 + min(costA, costB)]

            stack.append(lastPair)

        return stack[-1][1]