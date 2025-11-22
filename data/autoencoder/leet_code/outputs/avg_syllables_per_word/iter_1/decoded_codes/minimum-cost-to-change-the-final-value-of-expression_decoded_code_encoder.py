def evaluate_expression(expression):
    stack = []
    for e in expression:
        if e in '(&|':
            stack.append((e, 0))
        elif e == ')':
            last = stack.pop()
            stack.pop()  # remove '('
        else:  # '0' or '1'
            last = (e, 1)
        if stack and stack[-1][0] in '&|':
            op = stack.pop()[0]
            a, cA = stack.pop()
            b, cB = last
            if op == '&':
                if a == '0' and b == '0':
                    last = ('0', 1 + min(cA, cB))
                elif a == '0' and b == '1':
                    last = ('0', 1)
                elif a == '1' and b == '0':
                    last = ('0', 1)
                else:
                    last = ('1', min(cA, cB))
            else:  # '|'
                if a == '0' and b == '0':
                    last = ('0', min(cA, cB))
                elif a == '0' and b == '1':
                    last = ('1', 1)
                elif a == '1' and b == '0':
                    last = ('1', 1)
                else:
                    last = ('1', 1 + min(cA, cB))
        stack.append(last)
    return stack[-1][1]