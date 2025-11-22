from collections import defaultdict

def count_balanced_subsequences(nums1, nums2, MOD):
    n = len(nums1)
    dp = [defaultdict(int) for _ in range(n)]
    count = 0
    for i in range(n):
        dp[i][nums1[i]] += 1
        dp[i][-nums2[i]] += 1
        if i > 0:
            for bal, f in dp[i-1].items():
                dp[i][bal + nums1[i]] = (dp[i][bal + nums1[i]] + f) % MOD
                dp[i][bal - nums2[i]] = (dp[i][bal - nums2[i]] + f) % MOD
        count = (count + dp[i][0]) % MOD
    return count