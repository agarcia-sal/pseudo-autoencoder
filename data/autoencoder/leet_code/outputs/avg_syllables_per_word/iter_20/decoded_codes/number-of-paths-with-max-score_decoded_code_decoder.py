import math
from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        # dp[i][j] = [max_score, number_of_paths]
        dp = [[[float('-inf'), 0] for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = [0, 1]

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                cell = board[i][j]
                if cell == 'X' or cell == 'S':
                    continue
                value = 0 if cell == 'E' else int(cell)
                for dx, dy in [(1,0), (0,1), (1,1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        next_score, next_paths = dp[ni][nj]
                        if next_score == float('-inf'):
                            continue
                        current_score, current_paths = dp[i][j]
                        candidate_score = next_score + value
                        if candidate_score > current_score:
                            dp[i][j] = [candidate_score, next_paths]
                        elif candidate_score == current_score:
                            dp[i][j][1] = (dp[i][j][1] + next_paths) % MOD

        if dp[0][0][0] == float('-inf'):
            return [0,0]
        return dp[0][0]