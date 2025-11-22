def max_product(n):
    MOD = 10**9 + 7
    if n <= 3:
        return n
    t, r = divmod(n, 3)
    if r == 0:
        return pow(3, t, MOD)
    if r == 1:
        return (pow(3, t - 1, MOD) * 4) % MOD
    return (pow(3, t, MOD) * 2) % MOD