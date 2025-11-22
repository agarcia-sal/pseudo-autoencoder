class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for ch in expression:
            if ch in ('t', 'f', '!', '&', '|'):
                stk.append(ch)
            elif ch == ')':
                t = 0
                f = 0
                # Count consecutive t and f tokens on top of the stack
                while stk and stk[-1] in ('t', 'f'):
                    last = stk.pop()
                    if last == 't':
                        t += 1
                    else:
                        f += 1
                op = stk.pop()  # operator before parenthesis
                if op == '!':
                    c = 't' if f == 0 else 'f'
                elif op == '&':
                    c = 'f' if f > 0 else 't'
                else:  # op == '|'
                    c = 't' if t > 0 else 'f'
                stk.append(c)
        return stk[0] == 't'