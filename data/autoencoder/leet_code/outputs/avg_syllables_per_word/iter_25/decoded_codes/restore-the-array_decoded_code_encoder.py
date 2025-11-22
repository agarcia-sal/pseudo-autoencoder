class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1

        max_len = len(str(k))  # maximum length of substring to check

        for i in range(1, n + 1):
            start = max(0, i - max_len)
            for j in range(start, i):
                if s[j] != '0':
                    num = int(s[j:i])
                    if 1 <= num <= k:
                        dp[i] = (dp[i] + dp[j]) % MOD
                    elif num > k:
                        # Further longer substrings will only be bigger, so break early
                        break
        return dp[n]