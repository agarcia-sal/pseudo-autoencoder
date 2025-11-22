class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for ch in expression:
            if ch in ('t', 'f', '!', '&', '|'):
                stk.append(ch)
            elif ch == ')':
                t = 0
                f = 0
                # Count t and f inside the current expression
                while stk and stk[-1] in ('t', 'f'):
                    if stk[-1] == 't':
                        t += 1
                    else:
                        f += 1
                    stk.pop()
                op = stk.pop()  # operator before the '('
                if op == '!':
                    # NOT operator: if any f inside, result is t, else f
                    ch = 't' if f > 0 else 'f'
                elif op == '&':
                    # AND operator: if any f inside, result is f, else t
                    ch = 'f' if f > 0 else 't'
                else:  # op == '|'
                    # OR operator: if any t inside, result is t, else f
                    ch = 't' if t > 0 else 'f'
                stk.append(ch)
        return stk[0] == 't'