def scoreOfStudents(s, answers):
    def eval_expr(expr):
        tokens = []
        num = 0
        for c in expr:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                tokens.append(num)
                tokens.append(c)
                num = 0
        tokens.append(num)

        i = 1
        while i < len(tokens):
            if tokens[i] == '*':
                tokens[i - 1] = tokens[i - 1] * tokens[i + 1]
                del tokens[i:i + 2]
            else:
                i += 1

        res = tokens[0]
        i = 1
        while i < len(tokens):
            if tokens[i] == '+':
                res += tokens[i + 1]
            i += 2
        return res

    def possible(expr):
        if expr.isdigit():
            return {int(expr)}
        res = set()
        for i in range(1, len(expr), 2):
            L = possible(expr[:i])
            R = possible(expr[i + 1:])
            for l in L:
                for r in R:
                    if expr[i] == '+':
                        val = l + r
                    else:
                        val = l * r
                    if val <= 1000:
                        res.add(val)
        return res

    correct = eval_expr(s)
    poss = possible(s)
    pts = 0
    for a in answers:
        if a == correct:
            pts += 5
        elif a in poss:
            pts += 2
    return pts