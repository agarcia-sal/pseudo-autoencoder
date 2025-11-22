class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for c in expression:
            if c in {'t', 'f', '!', '&', '|'}:
                stk.append(c)
            elif c == ')':
                count_true = 0
                count_false = 0
                while stk and stk[-1] in {'t', 'f'}:
                    val = stk.pop()
                    if val == 't':
                        count_true += 1
                    else:  # val == 'f'
                        count_false += 1
                operator = stk.pop() if stk else None
                if operator == '!':
                    c = 't' if count_false > 0 else 'f'
                elif operator == '&':
                    c = 'f' if count_false > 0 else 't'
                elif operator == '|':
                    c = 't' if count_true > 0 else 'f'
                else:
                    # Defensive: Should not happen for valid input expression
                    c = 'f'
                stk.append(c)
        return stk[0] == 't'