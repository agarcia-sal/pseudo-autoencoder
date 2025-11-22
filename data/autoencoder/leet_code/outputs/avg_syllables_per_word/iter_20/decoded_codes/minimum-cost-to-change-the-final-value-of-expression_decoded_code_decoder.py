class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        stack = []
        for element in expression:
            if element in ('(', '&', '|'):
                stack.append([element, 0])
                continue

            if element == ')':
                last_pair = stack.pop()
                # Pop the operator
                operator = stack.pop()[0]
                # Pop the left operand and its cost
                a, cost_a = stack.pop()
                # last_pair is the right operand and its cost
                b, cost_b = last_pair

                if operator == '&':
                    if a == 0 and b == 0:
                        # Both False: result False with cost = 1 + min cost to flip either operand
                        last_pair = [0, 1 + min(cost_a, cost_b)]
                    elif (a == 0 and b == 1) or (a == 1 and b == 0):
                        # One False, one True: result False with cost 1
                        last_pair = [0, 1]
                    else:
                        # Both True: result True with cost = min cost to flip either operand
                        last_pair = [1, min(cost_a, cost_b)]
                else:  # operator == '|'
                    if a == 0 and b == 0:
                        # Both False: result False with cost = min cost to flip either operand
                        last_pair = [0, min(cost_a, cost_b)]
                    elif (a == 0 and b == 1) or (a == 1 and b == 0):
                        # One True, one False: result True with cost 1
                        last_pair = [1, 1]
                    else:
                        # Both True: result True with cost = 1 + min cost to flip either operand
                        last_pair = [1, 1 + min(cost_a, cost_b)]
            else:
                # element is '0' or '1'
                last_pair = [int(element), 1]

            # If the top of the stack is an operator ('&' or '|'), we try to combine it
            while (
                len(stack) >= 2
                and stack[-1][0] in (0, 1)
                and stack[-2][0] in ('&', '|')
                and len(stack) >= 3
                and stack[-3][0] in (0, 1)
            ):
                b, cost_b = stack.pop()
                operator = stack.pop()[0]
                a, cost_a = stack.pop()

                if operator == '&':
                    if a == 0 and b == 0:
                        last_pair = [0, 1 + min(cost_a, cost_b)]
                    elif (a == 0 and b == 1) or (a == 1 and b == 0):
                        last_pair = [0, 1]
                    else:
                        last_pair = [1, min(cost_a, cost_b)]
                else:  # operator == '|'
                    if a == 0 and b == 0:
                        last_pair = [0, min(cost_a, cost_b)]
                    elif (a == 0 and b == 1) or (a == 1 and b == 0):
                        last_pair = [1, 1]
                    else:
                        last_pair = [1, 1 + min(cost_a, cost_b)]

                stack.append(last_pair)

            else:
                stack.append(last_pair)

        return stack[-1][1]