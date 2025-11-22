def dp(l, r, memo):
    if l >= r:
        return 0
    if (l, r) in memo:
        return memo[(l, r)]
    memo[(l, r)] = min(
        p + max(dp(l, p - 1, memo), dp(p + 1, r, memo))
        for p in range(l, r + 1)
    )
    return memo[(l, r)]

def solve(n):
    memo = {}
    return dp(1, n, memo)