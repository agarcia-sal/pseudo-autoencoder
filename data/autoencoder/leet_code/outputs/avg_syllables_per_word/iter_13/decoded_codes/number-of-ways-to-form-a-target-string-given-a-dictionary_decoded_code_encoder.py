from collections import defaultdict
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n = len(words[0])
        m = len(target)

        freq = [defaultdict(int) for _ in range(n)]
        for word in words:
            for j, ch in enumerate(word):
                freq[j][ch] += 1

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                c = target[i - 1]
                f = freq[j - 1].get(c, 0)
                if f > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * f) % MOD

        return dp[m][n]