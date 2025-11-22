def minimum_white_tiles(floor, numCarpets, carpetLen):
    n = len(floor)
    dp = [[0] * (numCarpets + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = dp[i-1][0] + (floor[i-1] == '1')

    for j in range(1, numCarpets + 1):
        for i in range(1, n + 1):
            dp[i][j] = min(
                dp[i-1][j] + (floor[i-1] == '1'),
                dp[max(0, i - carpetLen)][j-1]
            )

    return dp[n][numCarpets]