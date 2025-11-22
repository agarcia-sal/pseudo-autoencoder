from math import inf
from typing import List

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def min_changes_to_palindrome(sub: str) -> int:
            i, j = 0, len(sub) - 1
            changes = 0
            while i < j:
                if sub[i] != sub[j]:
                    changes += 1
                i += 1
                j -= 1
            return changes

        n = len(s)
        # dp[i][j]: minimum changes to split first i chars into j palindromic substrings
        dp: List[List[int]] = [[inf] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            max_j = min(k, i)
            for j in range(1, max_j + 1):
                for start in range(i):
                    changes = min_changes_to_palindrome(s[start:i])
                    if dp[start][j - 1] != inf:
                        dp[i][j] = min(dp[i][j], dp[start][j - 1] + changes)

        return dp[n][k]