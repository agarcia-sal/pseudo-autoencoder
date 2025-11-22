class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for c in expression:
            if c in ('t', 'f', '!', '&', '|'):
                stk.append(c)
            elif c == ')':
                t_count = 0
                f_count = 0
                while stk and stk[-1] in ('t', 'f'):
                    val = stk.pop()
                    if val == 't':
                        t_count += 1
                    else:
                        f_count += 1
                op = stk.pop()  # operator just before '('
                if op == '!':
                    c = 't' if f_count != 0 else 'f'
                elif op == '&':
                    c = 'f' if f_count != 0 else 't'
                else:  # op == '|'
                    c = 't' if t_count != 0 else 'f'
                stk.append(c)
            # ignore other chars such as '('
        return stk[0] == 't'