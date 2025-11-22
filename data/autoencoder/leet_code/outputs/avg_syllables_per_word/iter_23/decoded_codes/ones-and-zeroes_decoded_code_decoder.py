from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j] represents the maximum number of strings that can be formed with i zeros and j ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            count_0 = s.count('0')
            count_1 = s.count('1')
            # Traverse dp in reverse to avoid using updated states in the current iteration
            for i in range(m, count_0 - 1, -1):
                for j in range(n, count_1 - 1, -1):
                    if dp[i][j] < dp[i - count_0][j - count_1] + 1:
                        dp[i][j] = dp[i - count_0][j - count_1] + 1
                    # else preserve the current value (no else clause needed since dp[i][j] already unchanged)
        return dp[m][n]