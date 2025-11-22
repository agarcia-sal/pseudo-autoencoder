class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MODULO = 10**9 + 7

        def initialize_two_dimensional_list(rows: int, columns: int) -> list:
            return [[0] * columns for _ in range(rows)]

        dp = initialize_two_dimensional_list(goal + 1, n + 1)
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                previous_count_for_new_song = dp[i - 1][j - 1]
                available_new_songs = n - (j - 1)
                dp[i][j] += previous_count_for_new_song * available_new_songs
                dp[i][j] %= MODULO

                if j > k:
                    previous_count_for_repeat_song = dp[i - 1][j]
                    available_repeat_songs = j - k
                    dp[i][j] += previous_count_for_repeat_song * available_repeat_songs
                    dp[i][j] %= MODULO

        return dp[goal][n]