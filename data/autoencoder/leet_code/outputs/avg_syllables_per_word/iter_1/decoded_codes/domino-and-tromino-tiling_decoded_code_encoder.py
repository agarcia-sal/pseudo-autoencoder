def solve(n):
    MOD = 10**9 + 7
    dp = [0] * (n + 1)
    dp1 = [0] * (n + 1)

    dp[0], dp[1] = 1, 1
    dp1[0], dp1[1] = 0, 0

    if n >= 2:
        dp[2] = 2
        dp1[2] = 1

    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2] + 2 * dp1[i-1]) % MOD
        dp1[i] = (dp[i-2] + dp1[i-1]) % MOD

    return dp[n]