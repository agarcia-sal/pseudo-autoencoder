from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0]) if strs else 0
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                # Check if column j is lexicographically <= column i for all rows k
                if all(strs[k][j] <= strs[k][i] for k in range(m)):
                    dp[i] = max(dp[i], dp[j] + 1)

        result = n - max(dp) if dp else 0
        return result