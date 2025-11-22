def atMostNGivenDigitSet(digits, n):
    str_n = str(n)
    L = len(str_n)
    d = len(digits)
    count = 0

    for l in range(1, L):
        count += d ** l

    for i in range(L):
        c = int(str_n[i])
        less = sum(1 for dig in digits if int(dig) < c)
        count += less * (d ** (L - i - 1))

        if not any(int(dig) == c for dig in digits):
            return count

    return count + 1