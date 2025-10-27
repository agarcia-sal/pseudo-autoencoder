class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for c in expression:
            if c in ('t', 'f', '!', '&', '|'):
                stk.append(c)
            elif c == ')':
                count_true = 0
                count_false = 0
                while stk and stk[-1] in ('t', 'f'):
                    if stk[-1] == 't':
                        count_true += 1
                    else:
                        count_false += 1
                    stk.pop()
                op = stk.pop()
                if op == '!':
                    c = 't' if count_false > 0 else 'f'
                elif op == '&':
                    c = 'f' if count_false > 0 else 't'
                else:  # op == '|'
                    c = 't' if count_true > 0 else 'f'
                stk.append(c)
        return stk[0] == 't'