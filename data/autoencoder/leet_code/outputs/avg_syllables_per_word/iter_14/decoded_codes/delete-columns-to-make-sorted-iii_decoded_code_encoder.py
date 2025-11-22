from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                # Check for all rows k whether strs[k][j] <= strs[k][i]
                if all(strs[k][j] <= strs[k][i] for k in range(m)):
                    dp[i] = max(dp[i], dp[j] + 1)

        longest_non_decreasing_subsequence_length = max(dp)
        result = n - longest_non_decreasing_subsequence_length
        return result