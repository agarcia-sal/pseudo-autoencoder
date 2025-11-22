from typing import List

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack: List[str] = []
        for ch in expression:
            if ch in ['t', 'f', '!', '&', '|', '(']:
                stack.append(ch)
            elif ch == ')':
                count_true = 0
                count_false = 0
                # Pop until '(' is found
                while stack and stack[-1] in ['t', 'f']:
                    val = stack.pop()
                    if val == 't':
                        count_true += 1
                    else:  # val == 'f'
                        count_false += 1
                # After popping literals, the next element must be '('
                if not stack or stack[-1] != '(':
                    # Defensive programming: malformed input expression
                    raise ValueError("Malformed expression: missing '(' before operator")
                stack.pop()  # remove '('

                if not stack:
                    raise ValueError("Malformed expression: missing operator")

                operator = stack.pop()

                if operator == '!':
                    # Negation: true if there is any false operand
                    result = 't' if count_false > 0 else 'f'
                elif operator == '&':
                    # Conjunction: false if any false operand
                    result = 'f' if count_false > 0 else 't'
                elif operator == '|':
                    # Disjunction: true if any true operand
                    result = 't' if count_true > 0 else 'f'
                else:
                    # Defensive programming: unexpected operator
                    raise ValueError(f"Unexpected operator: {operator}")

                stack.append(result)
        if len(stack) != 1:
            raise ValueError("Malformed expression: incomplete evaluation")
        return stack[0] == 't'