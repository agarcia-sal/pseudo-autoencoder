class Solution:
    def parseBoolExpr(self, expression):
        stk = []
        for c in expression:
            if c in ['t', 'f', '!', '&', '|']:
                stk.append(c)
            elif c == ')':
                t = 0
                f = 0
                while stk and (stk[-1] == 't' or stk[-1] == 'f'):
                    top = stk.pop()
                    if top == 't':
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
        return stk[-1] == 't'