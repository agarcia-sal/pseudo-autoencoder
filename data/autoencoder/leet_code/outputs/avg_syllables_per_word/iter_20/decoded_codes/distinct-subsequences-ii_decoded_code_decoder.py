class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        last = {}
        for i in range(1, n + 1):
            char = s[i - 1]
            dp[i] = (2 * dp[i - 1]) % MOD
            if char in last:
                dp[i] = (dp[i] - dp[last[char] - 1] + MOD) % MOD
            last[char] = i
        result = (dp[n] - 1) % MOD
        return result