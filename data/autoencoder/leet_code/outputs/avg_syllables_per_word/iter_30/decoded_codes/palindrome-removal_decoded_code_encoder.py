class Solution:
    def minimumMoves(self, arr: list[int]) -> int:
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
                    dp[i][j] = float('inf')
                    for k in range(i, j):
                        candidate = dp[i][k] + dp[k + 1][j]
                        if candidate < dp[i][j]:
                            dp[i][j] = candidate

        return dp[0][n - 1]