from collections import Counter
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n = len(words[0]) if words else 0
        m = len(target)

        freq = [Counter() for _ in range(n)]
        for word in words:
            for j, c in enumerate(word):
                freq[j][c] += 1

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            tgt_char = target[i - 1]
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                count = freq[j - 1].get(tgt_char, 0)
                if count > 0:
                    dp[i][j] += dp[i - 1][j - 1] * count
                    dp[i][j] %= MOD

        return dp[m][n]