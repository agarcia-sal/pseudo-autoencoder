class Solution:
    def numWays(self, words, target):
        MOD = 10**9 + 7
        n = len(words[0])
        m = len(target)

        # freq[j] is a dictionary mapping char -> count at position j in words
        freq = [{} for _ in range(n)]
        for word in words:
            for j, char in enumerate(word):
                freq[j][char] = freq[j].get(char, 0) + 1

        # dp[i][j]: number of ways to form target[:i] using first j characters of words' positions
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # empty string target can always be formed in one way
        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            target_char = target[i - 1]
            for j in range(1, n + 1):
                # ways without using position j-1
                dp[i][j] = dp[i][j - 1]
                count = freq[j - 1].get(target_char, 0)
                if count > 0:
                    dp[i][j] += dp[i - 1][j - 1] * count
                    dp[i][j] %= MOD

        return dp[m][n]