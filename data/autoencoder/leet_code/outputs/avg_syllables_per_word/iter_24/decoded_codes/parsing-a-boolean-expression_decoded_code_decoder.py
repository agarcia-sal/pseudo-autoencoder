class Solution:
    def parseBoolExpr(self, expression):
        stk = []
        for ch in expression:
            if ch in ('t', 'f', '!', '&', '|'):
                stk.append(ch)
            elif ch == ')':
                count_true = 0
                count_false = 0
                while stk and stk[-1] in ('t', 'f'):
                    if stk[-1] == 't':
                        count_true += 1
                    else:
                        count_false += 1
                    stk.pop()
                operator = stk.pop()
                if operator == '!':
                    ch = 't' if count_false > 0 else 'f'
                elif operator == '&':
                    ch = 'f' if count_false > 0 else 't'
                else:  # operator == '|'
                    ch = 't' if count_true > 0 else 'f'
                stk.append(ch)
        return stk[0] == 't'