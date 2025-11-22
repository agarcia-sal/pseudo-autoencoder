MOD = 10**9 + 7

def count_special_subsequences(nums):
    dp = [0, 0, 0]

    for n in nums:
        if n == 0:
            dp[0] = (2 * dp[0] + 1) % MOD
        elif n == 1:
            dp[1] = (2 * dp[1] + dp[0]) % MOD
        else:
            dp[2] = (2 * dp[2] + dp[1]) % MOD

    return dp[2]