from collections import defaultdict

class Solution:
    def numWays(self, words, target):
        MOD = 10**9 + 7
        n = len(words[0])
        m = len(target)

        freq = self.precompute_frequencies(words, n)
        dp = self.initialize_dp_table(m, n)
        self.set_base_case(dp, n)

        for i in range(1, m + 1):
            target_char = target[i - 1]
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                if target_char in freq[j - 1] and freq[j - 1][target_char] > 0:
                    dp[i][j] += dp[i - 1][j - 1] * freq[j - 1][target_char]
                    dp[i][j] %= MOD

        return dp[m][n]

    def precompute_frequencies(self, words, n):
        freq = [defaultdict(int) for _ in range(n)]
        for word in words:
            for j in range(n):
                char = word[j]
                freq[j][char] += 1
        return freq

    def initialize_dp_table(self, m, n):
        return [[0] * (n + 1) for _ in range(m + 1)]

    def set_base_case(self, dp, n):
        for j in range(n + 1):
            dp[0][j] = 1