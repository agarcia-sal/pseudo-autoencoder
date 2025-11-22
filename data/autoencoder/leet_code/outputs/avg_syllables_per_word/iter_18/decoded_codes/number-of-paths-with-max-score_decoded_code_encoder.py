class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 10**9 + 1
        n = len(board)

        dp = self.initialize_dp(n)
        self.set_starting_point(dp, n)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or board[i][j] == 'S':
                    continue

                value = self.get_cell_value(board, i, j)

                for x, y in [(1, 0), (0, 1), (1, 1)]:
                    ni = i + x
                    nj = j + y
                    if 0 <= ni < n and 0 <= nj < n:
                        if dp[ni][nj][0] > dp[i][j][0]:
                            dp[i][j][0] = dp[ni][nj][0] + value
                            dp[i][j][1] = dp[ni][nj][1]
                        elif dp[ni][nj][0] == dp[i][j][0]:
                            dp[i][j][1] = (dp[i][j][1] + dp[ni][nj][1]) % MOD

        if dp[0][0][0] == float('-inf'):
            return [0, 0]
        return [dp[0][0][0], dp[0][0][1]]

    def initialize_dp(self, n: int) -> list[list[list[int]]]:
        return [[ [float('-inf'), 0] for _ in range(n)] for __ in range(n)]

    def set_starting_point(self, dp: list[list[list[int]]], n: int) -> None:
        dp[n-1][n-1] = [0, 1]

    def get_cell_value(self, board: list[str], i: int, j: int) -> int:
        if board[i][j] != 'E':
            return int(board[i][j])
        return 0