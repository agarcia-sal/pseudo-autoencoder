class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = self.auxiliary_initialize_dp(n, goal)
        dp[0][0] = 1  # Base case: 0 songs in playlist with 0 unique songs chosen
        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                # Choosing a new unique song
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * (n - (j - 1))) % MOD
                # Choosing a song that has already been used, considering cooldown k
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD
        return dp[goal][n]

    def auxiliary_initialize_dp(self, n: int, goal: int) -> list[list[int]]:
        # Initialize a (goal+1) x (n+1) 2D list filled with zeros
        return [[0] * (n + 1) for _ in range(goal + 1)]