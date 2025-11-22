class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7

        def create_zero_matrix(rows: int, columns: int) -> list[list[int]]:
            matrix = []
            for _ in range(rows):
                matrix.append([0] * columns)
            return matrix

        dp = create_zero_matrix(goal + 1, n + 1)
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                dp[i][j] += dp[i - 1][j - 1] * (n - (j - 1))
                dp[i][j] %= MOD
                if j > k:
                    dp[i][j] += dp[i - 1][j] * (j - k)
                    dp[i][j] %= MOD

        return dp[goal][n]