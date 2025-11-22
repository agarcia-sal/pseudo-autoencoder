class Solution:
    def numWays(self, words, target):
        MOD = 10**9 + 7
        n = len(words[0])
        m = len(target)

        freq = [dict() for _ in range(n)]
        for word in words:
            for j, ch in enumerate(word):
                freq[j][ch] = freq[j].get(ch, 0) + 1

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            t_char = target[i - 1]
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                if freq[j - 1].get(t_char, 0) > 0:
                    dp[i][j] += dp[i - 1][j - 1] * freq[j - 1][t_char]
                    dp[i][j] %= MOD

        return dp[m][n]