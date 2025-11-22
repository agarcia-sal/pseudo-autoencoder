from typing import List
from collections import defaultdict

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 1
        n = len(words[0]) if words else 0
        m = len(target)

        freq = [defaultdict(int) for _ in range(n)]
        for word in words:
            if len(word) != n:
                # Words must all have the same length as per problem constraints,
                # but handle gracefully if not.
                continue
            for j, char in enumerate(word):
                freq[j][char] += 1

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = 1  # Empty target can be formed by any prefix

        for i in range(1, m + 1):
            target_char = target[i - 1]
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                count = freq[j - 1].get(target_char, 0)
                if count > 0:
                    dp[i][j] += dp[i - 1][j - 1] * count
                    dp[i][j] %= MOD

        return dp[m][n]