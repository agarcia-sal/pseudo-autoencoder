class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for c in expression:
            if c in 'tf!&|':
                stk.append(c)
            elif c == ')':
                t = 0
                f = 0
                while stk and stk[-1] in 'tf':
                    if stk[-1] == 't':
                        t += 1
                    else:
                        f += 1
                    stk.pop()
                op = stk.pop() if stk else None
                if op == '!':
                    c = 't' if f != 0 else 'f'
                elif op == '&':
                    c = 'f' if f != 0 else 't'
                elif op == '|':
                    c = 't' if t != 0 else 'f'
                else:
                    # This branch shouldn't be reached if input is valid
                    c = 'f'
                stk.append(c)
        return stk[-1] == 't' if stk else False