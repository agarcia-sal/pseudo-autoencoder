class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for c in expression:
            if c in ('t', 'f', '!', '&', '|'):
                stk.append(c)
            elif c == ')':
                t = f = 0
                while stk and stk[-1] in ('t', 'f'):
                    val = stk.pop()
                    t += val == 't'
                    f += val == 'f'
                op = stk.pop()
                if op == '!':
                    stk.append('t' if f > 0 else 'f')
                elif op == '&':
                    stk.append('f' if f > 0 else 't')
                else:  # op == '|'
                    stk.append('t' if t > 0 else 'f')
        return stk[0] == 't'