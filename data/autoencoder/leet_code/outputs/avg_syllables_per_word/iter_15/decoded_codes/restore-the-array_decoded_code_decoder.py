class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                # s[j] corresponds to the start of the substring
                if s[j] != '0':
                    num = int(s[j:i])
                    if 1 <= num <= k:
                        dp[i] = (dp[i] + dp[j]) % MOD
        return dp[n]