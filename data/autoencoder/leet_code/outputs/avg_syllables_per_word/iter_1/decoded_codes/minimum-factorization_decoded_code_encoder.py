def smallest_factorization(num):
    if num == 1:
        return 1
    factors = []
    for d in range(9, 1, -1):
        while num % d == 0:
            factors.append(d)
            num //= d
    if num != 1:
        return 0
    factors.sort()
    result = int(''.join(map(str, factors)))
    return result if result <= 2**31 - 1 else 0