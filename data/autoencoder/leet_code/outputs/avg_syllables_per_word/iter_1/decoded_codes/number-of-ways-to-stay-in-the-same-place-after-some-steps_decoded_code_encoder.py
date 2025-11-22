def num_ways(steps, arrLen):
    MOD = 10**9 + 7
    max_i = min(steps // 2, arrLen - 1)
    dp = [0] * (max_i + 1)
    dp[0] = 1
    for _ in range(steps):
        prev = dp[:]
        for i in range(max_i + 1):
            dp[i] = prev[i]
            if i > 0:
                dp[i] = (dp[i] + prev[i - 1]) % MOD
            if i < max_i:
                dp[i] = (dp[i] + prev[i + 1]) % MOD
    return dp[0]