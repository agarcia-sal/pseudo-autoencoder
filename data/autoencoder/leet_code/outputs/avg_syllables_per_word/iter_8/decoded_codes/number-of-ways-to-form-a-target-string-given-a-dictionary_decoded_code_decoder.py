class Solution:
    def numWays(self, words, target):
        MOD = 10**9 + 7
        n = len(words[0])
        m = len(target)

        freq = [dict() for _ in range(n)]
        for word in words:
            for j, char in enumerate(word):
                freq[j][char] = freq[j].get(char, 0) + 1

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                c = target[i - 1]
                count = freq[j - 1].get(c, 0)
                if count > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * count) % MOD

        return dp[m][n]