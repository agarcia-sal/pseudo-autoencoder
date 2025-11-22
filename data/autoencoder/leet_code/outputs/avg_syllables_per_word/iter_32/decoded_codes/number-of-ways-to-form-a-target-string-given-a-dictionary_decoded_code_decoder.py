from typing import List
from collections import Counter

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n = len(words[0])
        m = len(target)

        # freq[j] will be a mapping from character to its count at position j in words
        freq = [Counter() for _ in range(n)]
        for word in words:
            for j, ch in enumerate(word):
                freq[j][ch] += 1

        # dp[i][j]: number of ways to form first i chars of target using first j chars positions in words
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: zero-length target can be formed by any prefix in exactly 1 way
        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            target_char = target[i - 1]
            for j in range(1, n + 1):
                # ways without using the j-th position
                dp[i][j] = dp[i][j - 1]
                # if target_char appears at position j-1, add ways using that
                count = freq[j - 1].get(target_char, 0)
                if count > 0:
                    dp[i][j] += dp[i - 1][j - 1] * count
                    dp[i][j] %= MOD

        return dp[m][n]