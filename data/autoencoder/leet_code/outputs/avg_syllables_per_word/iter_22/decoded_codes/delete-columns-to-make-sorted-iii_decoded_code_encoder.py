class Solution:
    def minDeletionSize(self, strs):
        total_rows = len(strs)
        total_columns = len(strs[0])
        dp = [1] * total_columns
        for i in range(1, total_columns):
            for j in range(i):
                # Check if column j is <= column i for every row k
                if all(strs[k][j] <= strs[k][i] for k in range(total_rows)):
                    dp[i] = max(dp[i], dp[j] + 1)
        longest_non_decreasing_subsequence_length = max(dp)
        return total_columns - longest_non_decreasing_subsequence_length