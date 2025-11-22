from collections import Counter
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 1
        n = len(words[0])
        m = len(target)

        # freq[j] maps character to count of that character at position j in all words
        freq = [Counter() for _ in range(n)]
        for word in words:
            for j, ch in enumerate(word):
                freq[j][ch] += 1

        # dp[i][j] = number of ways to form first i chars of target using first j chars of words at each position
        # dp dimensions: (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # With 0 chars needed from target, there's exactly 1 way (choose nothing)
        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            current_char = target[i - 1]
            for j in range(1, n + 1):
                # ways without using j-th column of words
                dp[i][j] = dp[i][j - 1]
                current_freq = freq[j - 1].get(current_char, 0)
                if current_freq > 0:
                    # ways including j-th column: multiply ways to form i-1 chars using j-1 columns by frequency
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * current_freq) % MOD

        return dp[m][n]