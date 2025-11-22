def fractionToDecimal(n, d):
    sign = "-" if (n < 0) ^ (d < 0) else ""
    n, d = abs(n), abs(d)
    q, r = divmod(n, d)
    int_part = str(q)
    if r == 0:
        return sign + int_part
    seen = {}
    frac = []
    while r != 0:
        if r in seen:
            i = seen[r]
            return sign + int_part + "." + "".join(frac[:i]) + "(" + "".join(frac[i:]) + ")"
        seen[r] = len(frac)
        r *= 10
        q, r = divmod(r, d)
        frac.append(str(q))
    return sign + int_part + "." + "".join(frac)