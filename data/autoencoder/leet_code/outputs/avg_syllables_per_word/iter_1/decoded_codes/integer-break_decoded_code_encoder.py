def max_product(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        max_p = 0
        for j in range(1, i):
            max_p = max(max_p, j * dp[i - j], j * (i - j))
        dp[i] = max_p
    return dp[n]