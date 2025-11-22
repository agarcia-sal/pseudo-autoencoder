from math import inf
from typing import List, Tuple

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        # dp[i][j] = (max_score_from_i_j, num_paths_with_max_score)
        dp: List[List[Tuple[int, int]]] = [[(-inf, 0) for _ in range(n)] for _ in range(n)]
        dp[n - 1][n - 1] = (0, 1)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or board[i][j] == 'S':
                    continue

                value = 0 if board[i][j] == 'E' else int(board[i][j])
                best_score, ways = dp[i][j]

                for dx, dy in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        next_score, next_ways = dp[ni][nj]
                        if next_score == -inf:
                            continue
                        total_score = next_score + value
                        if total_score > best_score:
                            best_score = total_score
                            ways = next_ways
                        elif total_score == best_score:
                            ways = (ways + next_ways) % MOD

                dp[i][j] = (best_score, ways)

        if dp[0][0][0] == -inf:
            return [0, 0]
        return list(dp[0][0])