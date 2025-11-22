class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if all(strs[k][j] <= strs[k][i] for k in range(m)):
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
        longest_subsequence = max(dp)
        result = n - longest_subsequence
        return result