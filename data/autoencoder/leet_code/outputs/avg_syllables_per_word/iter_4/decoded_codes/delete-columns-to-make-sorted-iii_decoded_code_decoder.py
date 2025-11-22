class Solution:
    def minDeletionSize(self, strs):
        m = len(strs)
        n = len(strs[0])
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if all(strs[k][j] <= strs[k][i] for k in range(m)):
                    dp[i] = max(dp[i], dp[j] + 1)

        result = n - max(dp)
        return result