from typing import List

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk: List[str] = []
        # Characters representing true, false, negation, and, or
        TRUE_CHAR = 't'
        FALSE_CHAR = 'f'
        NOT_CHAR = '!'
        AND_CHAR = '&'
        OR_CHAR = '|'
        CLOSE_PAREN = ')'

        for c in expression:
            if c in (TRUE_CHAR, FALSE_CHAR, NOT_CHAR, AND_CHAR, OR_CHAR):
                stk.append(c)
            elif c == CLOSE_PAREN:
                count_true = 0
                count_false = 0
                # Count true/false in the current expression within parentheses
                while stk and stk[-1] in (TRUE_CHAR, FALSE_CHAR):
                    if stk[-1] == TRUE_CHAR:
                        count_true += 1
                    else:
                        count_false += 1
                    stk.pop()
                # Operator is just before the counted values
                operator = stk.pop() if stk else None

                if operator == NOT_CHAR:
                    # Negation: true if any false exists, else false
                    c = TRUE_CHAR if count_false > 0 else FALSE_CHAR
                elif operator == AND_CHAR:
                    # AND: false if any false exists, else true
                    c = FALSE_CHAR if count_false > 0 else TRUE_CHAR
                elif operator == OR_CHAR:
                    # OR: true if any true exists, else false
                    c = TRUE_CHAR if count_true > 0 else FALSE_CHAR
                else:
                    # Defensive: if operator somehow missing, fallback no-op
                    c = FALSE_CHAR
                stk.append(c)

        return stk[0] == TRUE_CHAR if stk else False