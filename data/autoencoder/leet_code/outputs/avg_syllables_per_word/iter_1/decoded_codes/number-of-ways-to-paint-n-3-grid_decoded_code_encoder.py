def compute(n):
    MOD = 10**9 + 7
    a, b = 6, 6
    for i in range(2, n + 1):
        a, b = (3 * a + 2 * b) % MOD, (2 * a + 2 * b) % MOD
    return (a + b) % MOD