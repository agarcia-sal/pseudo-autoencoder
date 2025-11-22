def brace_expansion(expr):
    def parse_expr(i):
        cur_set = set()
        cur_prod = [""]
        while i < len(expr):
            c = expr[i]
            if c == '{':
                inner_set, i = parse_expr(i + 1)
                cur_prod = [a + b for a in cur_prod for b in inner_set]
            elif c == '}':
                cur_set.update(cur_prod)
                return cur_set, i
            elif c == ',':
                cur_set.update(cur_prod)
                cur_prod = [""]
            else:
                cur_prod = [a + c for a in cur_prod]
            i += 1
        cur_set.update(cur_prod)
        return cur_set, i

    res, _ = parse_expr(0)
    return sorted(res)