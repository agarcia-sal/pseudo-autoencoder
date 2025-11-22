class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for ch in expression:
            if ch in ('t', 'f', '!', '&', '|'):
                stk.append(ch)
            elif ch == ')':
                t = 0
                f = 0
                while stk and stk[-1] in ('t', 'f'):
                    val = stk.pop()
                    if val == 't':
                        t += 1
                    else:
                        f += 1
                op = stk.pop()
                if op == '!':
                    ch = 't' if f > 0 else 'f'
                elif op == '&':
                    ch = 'f' if f > 0 else 't'
                else:  # op == '|'
                    ch = 't' if t > 0 else 'f'
                stk.append(ch)
        return stk[0] == 't'