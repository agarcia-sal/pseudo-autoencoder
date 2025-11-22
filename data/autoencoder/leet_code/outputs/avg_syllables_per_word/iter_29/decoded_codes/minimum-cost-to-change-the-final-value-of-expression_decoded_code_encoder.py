class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        stack = []
        for element in expression:
            if element in ('(', '&', '|'):
                stack.append([element, 0])
                continue

            if element == ')':
                lastPair = stack.pop()
                stack.pop()
            else:
                lastPair = [element, 1]

            if stack and stack[-1][0] in ('&', '|'):
                op = stack.pop()[0]
                a, costA = stack.pop()
                b, costB = lastPair

                if op == '&':
                    if a == '0' and b == '0':
                        lastPair = ['0', 1 + min(costA, costB)]
                    elif (a == '0' and b == '1') or (a == '1' and b == '0'):
                        lastPair = ['0', 1]
                    else:
                        lastPair = ['1', min(costA, costB)]
                else:
                    if a == '0' and b == '0':
                        lastPair = ['0', min(costA, costB)]
                    elif (a == '0' and b == '1') or (a == '1' and b == '0'):
                        lastPair = ['1', 1]
                    else:
                        lastPair = ['1', 1 + min(costA, costB)]

            stack.append(lastPair)

        return stack[-1][1]