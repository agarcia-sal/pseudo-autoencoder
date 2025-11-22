from collections import defaultdict
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        n = len(words[0])
        m = len(target)

        # freq[j]: dictionary mapping char -> frequency of that char at position j in words
        freq = [defaultdict(int) for _ in range(n)]
        for word in words:
            for j, ch in enumerate(word):
                freq[j][ch] += 1

        # dp[i][j]: number of ways to form target[:i] using characters from columns [:j] of words
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # base case: zero length target can be formed in exactly 1 way from any prefix of words
        for j in range(n + 1):
            dp[0][j] = 1

        for i in range(1, m + 1):
            target_char = target[i - 1]
            for j in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]
                freq_count = freq[j - 1].get(target_char, 0)
                if freq_count > 0:
                    dp[i][j] += dp[i - 1][j - 1] * freq_count
                dp[i][j] %= MOD

        return dp[m][n]