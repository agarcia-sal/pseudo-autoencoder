def ambiguousCoordinates(s):
    def make(f):
        for d in range(1, len(f) + 1):
            left, right = f[:d], f[d:]
            if (left == "0" or not left.startswith("0")) and (not right.endswith("0")):
                yield left + ("." if d < len(f) else "") + right

    s = s[1:-1]
    return ["(" + a + ", " + b + ")" 
            for i in range(1, len(s)) 
            for a in make(s[:i]) 
            for b in make(s[i:])]