class Solution:
    def minimumMoves(self, arr):
        n = len(arr)
        dp = self.createTwoDimensionalList(0, n)

        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1):
            if arr[i] == arr[i + 1]:
                dp[i][i + 1] = 1
            else:
                dp[i][i + 1] = 2

        for length in range(3, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                if arr[start] == arr[end]:
                    dp[start][end] = dp[start + 1][end - 1]
                else:
                    dp[start][end] = float('inf')
                    for mid in range(start, end):
                        val = dp[start][mid] + dp[mid + 1][end]
                        if val < dp[start][end]:
                            dp[start][end] = val

        return dp[0][n - 1]

    def createTwoDimensionalList(self, initial_value, dimension_size):
        return [[initial_value for _ in range(dimension_size)] for __ in range(dimension_size)]