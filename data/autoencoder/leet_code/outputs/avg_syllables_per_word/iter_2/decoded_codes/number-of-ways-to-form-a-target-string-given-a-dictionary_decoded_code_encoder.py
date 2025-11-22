from typing import List
from collections import defaultdict

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n = len(words[0])
        m = len(target)

        freq = [defaultdict(int) for _ in range(n)]
        for word in words:
            for j in range(n):
                freq[j][word[j]] += 1

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                c = target[i - 1]
                if freq[j - 1][c] > 0:
                    dp[i][j] += dp[i - 1][j - 1] * freq[j - 1][c]
                    dp[i][j] %= MOD

        return dp[m][n]