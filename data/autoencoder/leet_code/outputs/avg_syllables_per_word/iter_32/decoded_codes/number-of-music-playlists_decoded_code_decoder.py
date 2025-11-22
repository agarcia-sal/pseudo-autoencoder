from typing import List

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7

        # dp[i][j] = number of playlists of length i with exactly j unique songs
        dp: List[List[int]] = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                # Add a new unique song to the playlist
                dp[i][j] += dp[i - 1][j - 1] * (n - (j - 1))
                dp[i][j] %= MOD

                # Reuse a song that was played at least k songs ago
                if j > k:
                    dp[i][j] += dp[i - 1][j] * (j - k)
                    dp[i][j] %= MOD

        return dp[goal][n]