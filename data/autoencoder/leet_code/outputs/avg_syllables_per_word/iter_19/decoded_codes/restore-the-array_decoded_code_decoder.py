class Solution:
    def numberOfArrays(self, s, k):
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        max_len = len(str(k))  # Max length of substring to consider

        for i in range(1, n + 1):
            # Only consider j such that substring s[j:i] length <= max_len for efficiency
            start = max(0, i - max_len)
            for j in range(start, i):
                if s[j] != '0':
                    substring_value = int(s[j:i])
                    if 1 <= substring_value <= k:
                        dp[i] = (dp[i] + dp[j]) % MOD
        return dp[n]