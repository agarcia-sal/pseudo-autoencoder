class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for c in expression:
            if c in 'tf!&|':
                stk.append(c)
            elif c == ')':
                t = 0
                f = 0
                while stk[-1] in 'tf':
                    val = stk.pop()
                    if val == 't':
                        t += 1
                    else:
                        f += 1
                op = stk.pop()
                if op == '!':
                    c = 't' if f > 0 else 'f'
                elif op == '&':
                    c = 'f' if f > 0 else 't'
                elif op == '|':
                    c = 't' if t > 0 else 'f'
                stk.append(c)
        return stk[0] == 't'