class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            # To optimize, limit j to maximum length of k in digits to avoid unnecessary checks
            max_len = len(str(k))
            for j in range(max(0, i - max_len), i):
                if s[j] != '0':
                    num = int(s[j:i])
                    if 1 <= num <= k:
                        dp[i] = (dp[i] + dp[j]) % MOD
        return dp[n]