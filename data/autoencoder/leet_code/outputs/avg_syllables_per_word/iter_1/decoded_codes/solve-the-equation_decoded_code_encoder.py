def solve_equation(eq):
    def parse_side(s):
        tokens = []
        i = 0
        while i < len(s):
            j = i
            if s[j] in '+-':
                j += 1
            while j < len(s) and s[j] not in '+-':
                j += 1
            tokens.append(s[i:j])
            i = j

        x_cnt, n_sum = 0, 0
        for t in tokens:
            if not t:
                continue
            if 'x' in t:
                if t in ['x', '+x']:
                    x_cnt += 1
                elif t == '-x':
                    x_cnt -= 1
                else:
                    x_cnt += int(t.replace('x',''))
            else:
                n_sum += int(t)
        return x_cnt, n_sum

    L, R = eq.split('=')
    Lx, Ln = parse_side(L)
    Rx, Rn = parse_side(R)
    X = Lx - Rx
    N = Rn - Ln

    if X == 0:
        if N == 0:
            return "Infinite solutions"
        else:
            return "No solution"
    else:
        return "x=" + str(N // X)