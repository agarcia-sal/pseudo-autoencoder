class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for c in expression:
            if c in ('t', 'f', '!', '&', '|'):
                stk.append(c)
            elif c == ')':
                t = f = 0
                while stk and stk[-1] in ('t', 'f'):
                    top = stk.pop()
                    if top == 't':
                        t += 1
                    else:
                        f += 1
                op = stk.pop()  # operator before '(' operand list
                if op == '!':
                    c = 't' if f == 0 else 'f'
                elif op == '&':
                    c = 'f' if f > 0 else 't'
                else:  # op == '|'
                    c = 't' if t > 0 else 'f'
                stk.append(c)
        return stk[0] == 't'