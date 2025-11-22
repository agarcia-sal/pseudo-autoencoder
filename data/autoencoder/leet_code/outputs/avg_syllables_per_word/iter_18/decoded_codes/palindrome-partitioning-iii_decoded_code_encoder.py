class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def min_changes_to_palindrome(sub: str) -> int:
            left_index, right_index = 0, len(sub) - 1
            changes_count = 0
            while left_index < right_index:
                if sub[left_index] != sub[right_index]:
                    changes_count += 1
                left_index += 1
                right_index -= 1
            return changes_count

        string_length = len(s)
        # dp[i][j]: minimum changes to partition first i chars into j palindromes
        dp = [[float('inf')] * (k + 1) for _ in range(string_length + 1)]
        dp[0][0] = 0

        for index_i in range(1, string_length + 1):
            for index_j in range(1, min(k, index_i) + 1):
                for start_position in range(index_i):
                    changes_needed = min_changes_to_palindrome(s[start_position:index_i])
                    compare_value = dp[start_position][index_j - 1] + changes_needed
                    if compare_value < dp[index_i][index_j]:
                        dp[index_i][index_j] = compare_value
        return dp[string_length][k]