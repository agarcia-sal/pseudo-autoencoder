class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        stack = []
        for e in expression:
            if e == '(' or e == '&' or e == '|':
                stack.append([e, 0])
                continue
            if e == ')':
                last_pair = stack.pop()
            else:
                last_pair = [e, 1]

            if stack and stack[-1][0] in {'&', '|'}:
                op = stack.pop()[0]
                a, cost_a = stack.pop()
                b, cost_b = last_pair
                if op == '&':
                    if a == '0' and b == '0':
                        last_pair = ['0', 1 + min(cost_a, cost_b)]
                    elif (a == '0' and b == '1') or (a == '1' and b == '0'):
                        last_pair = ['0', 1]
                    else:
                        last_pair = ['1', min(cost_a, cost_b)]
                else:
                    # op == '|'
                    if a == '0' and b == '0':
                        last_pair = ['0', min(cost_a, cost_b)]
                    elif (a == '0' and b == '1') or (a == '1' and b == '0'):
                        last_pair = ['1', 1]
                    else:
                        last_pair = ['1', 1 + min(cost_a, cost_b)]
            stack.append(last_pair)
        return stack[-1][1]