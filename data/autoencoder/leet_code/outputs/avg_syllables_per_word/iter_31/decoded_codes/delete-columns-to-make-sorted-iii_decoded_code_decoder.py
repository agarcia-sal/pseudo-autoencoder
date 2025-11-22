from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        if m == 0:
            return 0
        n = len(strs[0])
        # dp[i] will hold the length of longest non-decreasing subsequence ending at index i
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if all(strs[k][j] <= strs[k][i] for k in range(m)):
                    dp[i] = max(dp[i], dp[j] + 1)

        longest_non_decreasing_subsequence = max(dp) if dp else 0
        return n - longest_non_decreasing_subsequence