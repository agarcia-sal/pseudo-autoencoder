from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        number_of_rows = len(strs)
        number_of_columns = len(strs[0]) if strs else 0
        dp = [1] * number_of_columns

        for i in range(1, number_of_columns):
            for j in range(i):
                # Check if column j <= column i for all rows
                if all(strs[k][j] <= strs[k][i] for k in range(number_of_rows)):
                    dp[i] = max(dp[i], dp[j] + 1)

        longest_non_decreasing_subsequence = max(dp) if dp else 0
        return number_of_columns - longest_non_decreasing_subsequence