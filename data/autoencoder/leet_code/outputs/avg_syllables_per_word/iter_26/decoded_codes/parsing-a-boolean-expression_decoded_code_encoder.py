class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for char in expression:
            if char in ('t', 'f', '!', '&', '|'):
                stk.append(char)
            elif char == ')':
                count_true, count_false = 0, 0
                while stk and stk[-1] in ('t', 'f'):
                    val = stk.pop()
                    if val == 't':
                        count_true += 1
                    else:
                        count_false += 1
                operator = stk.pop()  # operator: '!', '&', '|'
                if operator == '!':
                    # NOT operator: true if count_false > 0 else false
                    res = 't' if count_false > 0 else 'f'
                elif operator == '&':
                    # AND operator: false if any false else true
                    res = 'f' if count_false > 0 else 't'
                else:  # operator == '|'
                    # OR operator: true if any true else false
                    res = 't' if count_true > 0 else 'f'
                stk.append(res)
        return stk[0] == 't'