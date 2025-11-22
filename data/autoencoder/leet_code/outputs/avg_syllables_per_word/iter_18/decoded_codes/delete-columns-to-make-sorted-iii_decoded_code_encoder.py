from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if all(strs[k][j] <= strs[k][i] for k in range(m)):
                    dp[i] = max(dp[i], dp[j] + 1)
        longest_non_decreasing_subsequence_length = max(dp)
        return n - longest_non_decreasing_subsequence_length