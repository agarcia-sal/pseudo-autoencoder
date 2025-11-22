from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        if m == 0:
            return 0
        n = len(strs[0])
        if any(len(s) != n for s in strs):
            # All strings should be of the same length by problem constraints,
            # but handle gracefully if not
            return 0

        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if all(strs[k][j] <= strs[k][i] for k in range(m)):
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1

        return n - max(dp)