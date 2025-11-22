def max_average_partition(nums, k):
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    def average(i, j):
        return (prefix_sum[j + 1] - prefix_sum[i]) / (j - i + 1)

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n):
        dp[i][1] = average(i, n - 1)

    for i in range(n - 1, -1, -1):
        for p in range(2, k + 1):
            for j in range(i + 1, n):
                dp[i][p] = max(dp[i][p], dp[j][p - 1] + average(i, j - 1))

    return dp[0][k]