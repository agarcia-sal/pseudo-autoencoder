def diffWaysToCompute(expr):
    def compute(L, R, op):
        res = []
        for l in L:
            for r in R:
                if op == '+':
                    res.append(l + r)
                elif op == '-':
                    res.append(l - r)
                else:  # op == '*'
                    res.append(l * r)
        return res

    def helper(sub):
        if sub.isdigit():
            return [int(sub)]
        res = []
        for i in range(len(sub)):
            if sub[i] in "+-*":
                L = helper(sub[:i])
                R = helper(sub[i+1:])
                res.extend(compute(L, R, sub[i]))
        return res

    return helper(expr)