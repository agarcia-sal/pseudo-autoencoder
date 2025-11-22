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
                    else:
                        count_false += 1
                operator = stk.pop()
                if operator == '!':
                    # NOT operator: true if any false was inside is false else true -> so invert
                    c = 't' if count_false == 0 else 'f'
                    # but original pseudocode says: c = t if count_false > 0 == false else f
                    # which means c = 't' if count_false == 0 else 'f'
                elif operator == '&':
                    c = 'f' if count_false > 0 else 't'
                elif operator == '|':
                    c = 't' if count_true > 0 else 'f'
                stk.append(c)
        return stk[0] == 't'