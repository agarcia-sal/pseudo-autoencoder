import math
from typing import List

class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1):
            if arr[i] == arr[i + 1]:
                dp[i][i + 1] = 1
            else:
                dp[i][i + 1] = 2

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if arr[i] == arr[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = math.inf
                    for k in range(i, j):
                        dp_candidate = dp[i][k] + dp[k + 1][j]
                        if dp_candidate < dp[i][j]:
                            dp[i][j] = dp_candidate

        return dp[0][n - 1] if n > 0 else 0