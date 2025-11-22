def findMaxForm(strs, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for s in strs:
        c0 = s.count('0')
        c1 = s.count('1')
        for i in range(m, c0 - 1, -1):
            for j in range(n, c1 - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - c0][j - c1] + 1)
    return dp[m][n]