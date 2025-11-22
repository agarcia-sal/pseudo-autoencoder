def generate_strobogrammatic(n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1", "8"]

    middles = generate_strobogrammatic(n - 2, length)
    res = []
    for m in middles:
        if n != length:
            res.append("0" + m + "0")
        res.append("1" + m + "1")
        res.append("6" + m + "9")
        res.append("8" + m + "8")
        res.append("9" + m + "6")
    return res


def count_strobogrammatic(low, high):
    c = 0
    for l in range(len(low), len(high) + 1):
        for num in generate_strobogrammatic(l, l):
            if (l == len(low) and num < low) or (l == len(high) and num > high):
                continue
            c += 1
    return c