class Solution:
    def numberOfArrays(self, string_s: str, integer_k: int) -> int:
        MOD = 10**9 + 1
        n = len(string_s)

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(i):
                if string_s[j] != '0':
                    num = int(string_s[j:i])
                    if 1 <= num <= integer_k:
                        dp[i] = (dp[i] + dp[j]) % MOD

        return dp[n]