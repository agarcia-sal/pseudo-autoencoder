class Solution:
    def minDeletionSize(self, strs):
        number_of_rows = len(strs)
        number_of_columns = len(strs[0])
        dp = [1] * number_of_columns

        for i in range(1, number_of_columns):
            for j in range(i):
                condition_to_check = True
                for k in range(number_of_rows):
                    if strs[k][j] > strs[k][i]:
                        condition_to_check = False
                        break
                if condition_to_check and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

        longest_non_decreasing_subsequence_length = max(dp)
        result = number_of_columns - longest_non_decreasing_subsequence_length
        return result