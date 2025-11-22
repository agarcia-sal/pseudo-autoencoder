def min_partitions(arr):
    n = len(arr)
    dp = [[0]*n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1
    for i in range(n-1):
        dp[i][i+1] = 1 if arr[i] == arr[i+1] else 2

    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i][k] + dp[k+1][j] for k in range(i, j))

    return dp[0][n-1]