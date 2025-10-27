class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for c in expression:
            if c in ('t', 'f', '!', '&', '|'):
                stk.append(c)
            elif c == ')':
                count_t = 0
                count_f = 0
                while stk and stk[-1] in ('t', 'f'):
                    val = stk.pop()
                    if val == 't':
                        count_t += 1
                    else:
                        count_f += 1
                operator = stk.pop()
                if operator == '!':
                    c = True if count_f > 0 is False else False
                    # The pseudocode logic: "SET c TO true IF count_f GREATER THAN zero IS false ELSE false"
                    # This means: c = true if not(count_f > 0), else false
                    # So correct interpretation:
                    c = not (count_f > 0)
                elif operator == '&':
                    c = False if count_f > 0 else True
                else:  # operator == '|'
                    c = True if count_t > 0 else False
                stk.append('t' if c else 'f')
        return stk[0] == 't'