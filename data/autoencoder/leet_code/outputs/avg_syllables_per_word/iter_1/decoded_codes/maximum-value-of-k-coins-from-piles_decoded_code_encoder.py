def max_value_from_piles(piles, k):
    n = len(piles)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            current_value = 0
            for l in range(0, min(j, len(piles[i-1])) + 1):
                if l > 0:
                    current_value += piles[i-1][l-1]
                dp[i][j] = max(dp[i][j], dp[i-1][j-l] + current_value)

    return dp[n][k]