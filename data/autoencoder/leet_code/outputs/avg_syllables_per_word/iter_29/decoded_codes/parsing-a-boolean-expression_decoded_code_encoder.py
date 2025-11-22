class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for ch in expression:
            if ch in {'t', 'f', '!', '&', '|'}:
                stack.append(ch)
            elif ch == ')':
                count_true = 0
                count_false = 0
                # Pop all boolean values until we reach an operator (!, &, |)
                while stack and stack[-1] in {'t', 'f'}:
                    val = stack.pop()
                    if val == 't':
                        count_true += 1
                    else:
                        count_false += 1
                operator = stack.pop()
                if operator == '!':
                    # Negation: true if no false, false otherwise
                    ch = 't' if count_false == 0 else 'f'
                elif operator == '&':
                    # AND: false if any false, true otherwise
                    ch = 'f' if count_false > 0 else 't'
                else:  # operator == '|'
                    # OR: true if any true, false otherwise
                    ch = 't' if count_true > 0 else 'f'
                stack.append(ch)
        return stack[0] == 't'