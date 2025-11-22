class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stk = []
        for ch in expression:
            if ch in {'t', 'f', '!', '&', '|'}:
                stk.append(ch)
            elif ch == ')':
                true_count = 0
                false_count = 0
                while stk and stk[-1] in {'t', 'f'}:
                    val = stk.pop()
                    if val == 't':
                        true_count += 1
                    else:
                        false_count += 1
                operator = stk.pop()
                if operator == '!':
                    ch = 't' if false_count > 0 else 'f'
                elif operator == '&':
                    ch = 'f' if false_count > 0 else 't'
                elif operator == '|':
                    ch = 't' if true_count > 0 else 'f'
                stk.append(ch)
        return stk[0] == 't'