class Solution:
    def distinctSubseqII(self, string_s: str) -> int:
        MOD = 10**9 + 7
        n = len(string_s)
        dp = [0] * (n + 1)
        dp[0] = 1

        last = {}

        for i in range(1, n + 1):
            char = string_s[i - 1]
            dp[i] = (dp[i - 1] * 2) % MOD
            if char in last:
                dp[i] = (dp[i] - dp[last[char] - 1] + MOD) % MOD
            last[char] = i

        return (dp[n] - 1) % MOD