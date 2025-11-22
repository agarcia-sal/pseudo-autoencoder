class Solution:
    def parseBoolExpr(self, expression):
        stk = []
        for c in expression:
            if c in ('t', 'f', '!', '&', '|'):
                stk.append(c)
            elif c == ')':
                t = 0
                f = 0
                # Count true and false values inside the current expression
                while stk and stk[-1] in ('t', 'f'):
                    val = stk.pop()
                    if val == 't':
                        t += 1
                    else:
                        f += 1
                op = stk.pop()  # operator before '('
                if op == '!':
                    c = 't' if f > 0 else 'f'
                elif op == '&':
                    c = 'f' if f > 0 else 't'
                else:  # op == '|'
                    c = 't' if t > 0 else 'f'
                stk.append(c)
        return stk[0] == 't'