def compute_value(n):
    MOD = 10**9 + 7
    if n == 1:
        return 0
    if n == 2:
        return 1
    prev2 = 0
    prev1 = 1
    for i in range(3, n + 1):
        current = (i - 1) * (prev1 + prev2) % MOD
        prev2 = prev1
        prev1 = current
    return prev1