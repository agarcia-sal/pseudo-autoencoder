def evaluate_bool_expr(expr):
    stk = []
    for c in expr:
        if c in {'t', 'f', '!', '&', '|'}:
            stk.append(c)
        elif c == ')':
            t = f = 0
            while stk and stk[-1] in {'t', 'f'}:
                top = stk.pop()
                t += (top == 't')
                f += (top == 'f')
            op = stk.pop()
            if op == '!':
                c = 't' if f == 0 else 'f'
            elif op == '&':
                c = 'f' if f > 0 else 't'
            elif op == '|':
                c = 't' if t > 0 else 'f'
            stk.append(c)
    return stk[0] == 't'