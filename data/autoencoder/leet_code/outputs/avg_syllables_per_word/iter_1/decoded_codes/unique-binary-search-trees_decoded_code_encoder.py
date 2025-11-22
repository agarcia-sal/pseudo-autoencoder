def catalan_number(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = sum(dp[j - 1] * dp[i - j] for j in range(1, i + 1))
    return dp[n]