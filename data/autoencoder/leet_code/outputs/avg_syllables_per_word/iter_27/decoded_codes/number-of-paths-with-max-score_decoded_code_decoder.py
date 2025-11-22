from math import inf
from typing import List, Tuple

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        # dp[i][j] = (max_score, count_of_ways)
        dp: List[List[Tuple[int, int]]] = [[(-inf, 0) for _ in range(n)] for _ in range(n)]

        dp[n-1][n-1] = (0, 1)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                c = board[i][j]
                if c == 'X' or c == 'S':
                    continue

                value = 0 if c == 'E' else int(c)

                curr_score, curr_count = dp[i][j]

                for x, y in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < n:
                        next_score, next_count = dp[ni][nj]
                        if next_score > curr_score:
                            dp[i][j] = (next_score + value, next_count)
                            curr_score, curr_count = dp[i][j]
                        elif next_score == curr_score and next_score != -inf:
                            dp[i][j] = (curr_score, (curr_count + next_count) % MOD)
                            curr_score, curr_count = dp[i][j]

        if dp[0][0][0] == -inf:
            return [0, 0]
        return [dp[0][0][0], dp[0][0][1]]