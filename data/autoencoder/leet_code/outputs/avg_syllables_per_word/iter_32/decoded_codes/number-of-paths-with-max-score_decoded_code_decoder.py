from math import inf
from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        # dp[i][j] = [max_score, count_paths]
        # max_score initialized to -inf, count_paths to 0
        dp = [[[-inf, 0] for _ in range(n)] for _ in range(n)]

        # Start position S is at bottom-right corner as per original pseudocode,
        # set dp at this position to [0, 1]
        dp[n - 1][n - 1] = [0, 1]

        # Moves: down (1,0), right (0,1), diagonally down-right (1,1)
        moves = [(1, 0), (0, 1), (1, 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                cell = board[i][j]
                # Skip 'X' and start 'S'
                if cell == 'X' or cell == 'S':
                    continue

                value = 0 if cell == 'E' else int(cell)

                for dx, dy in moves:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        ni_score, ni_count = dp[ni][nj]
                        if ni_score == -inf:
                            continue
                        new_score = ni_score + value
                        curr_score, curr_count = dp[i][j]
                        if new_score > curr_score:
                            dp[i][j] = [new_score, ni_count]
                        elif new_score == curr_score:
                            dp[i][j][1] = (dp[i][j][1] + ni_count) % MOD

        if dp[0][0][0] == -inf:
            return [0, 0]
        return dp[0][0]