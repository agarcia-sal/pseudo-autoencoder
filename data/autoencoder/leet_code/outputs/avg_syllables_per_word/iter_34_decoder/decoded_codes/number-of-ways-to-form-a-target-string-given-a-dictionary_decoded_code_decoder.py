from collections import Counter
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n = len(words[0])
        m = len(target)

        # freq[j] = Counter of characters at position j among all words
        freq = [Counter() for _ in range(n)]
        for word in words:
            for j, char in enumerate(word):
                freq[j][char] += 1

        # dp[i][j] = number of ways to form target[:i] using first j characters of words
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = 1  # empty target can always be formed

        for i in range(1, m + 1):
            target_char = target[i - 1]
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                freq_val = freq[j - 1].get(target_char, 0)
                if freq_val > 0:
                    dp[i][j] += dp[i - 1][j - 1] * freq_val
                    dp[i][j] %= MOD

        return dp[m][n]