class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        k_str = str(k)
        max_len = len(k_str)
        for i in range(1, n + 1):
            # Consider all substrings ending at i-1, starting from j
            start = max(0, i - max_len)
            for j in range(start, i):
                if s[j] != '0':
                    num_str = s[j:i]
                    # Compare lengths first, then lexicographically if lengths equal to avoid int conversion overhead
                    if len(num_str) < max_len or (len(num_str) == max_len and num_str <= k_str):
                        dp[i] = (dp[i] + dp[j]) % MOD
        return dp[n]