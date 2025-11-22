def min_cost(cost):
    size1, size2 = len(cost), len(cost[0])
    dp = [[float('inf')] * (1 << size2) for _ in range(size1 + 1)]
    dp[0][0] = 0

    for i in range(size1):
        for mask in range(1 << size2):
            for j in range(size2):
                dp[i + 1][mask | (1 << j)] = min(dp[i + 1][mask | (1 << j)], dp[i][mask] + cost[i][j])
            for j in range(size2):
                if mask & (1 << j):
                    dp[i + 1][mask] = min(dp[i + 1][mask], dp[i + 1][mask ^ (1 << j)] + cost[i][j])

    return dp[size1][(1 << size2) - 1]