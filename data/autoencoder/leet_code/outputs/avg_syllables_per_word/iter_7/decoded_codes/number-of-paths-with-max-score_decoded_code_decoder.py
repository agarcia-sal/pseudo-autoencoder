from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        NEG_INF = float('-inf')

        dp: List[List[List[int]]] = [[[NEG_INF, 0] for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = [0, 1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or board[i][j] == 'S':
                    continue
                value = 0 if board[i][j] == 'E' else int(board[i][j])

                for x, y in [(1, 0), (0, 1), (1, 1)]:
                    ni, nj = i + x, j + y
                    if 0 <= ni < n and 0 <= nj < n:
                        if dp[ni][nj][0] == NEG_INF:
                            continue
                        current_score = dp[ni][nj][0] + value
                        if current_score > dp[i][j][0]:
                            dp[i][j] = [current_score, dp[ni][nj][1]]
                        elif current_score == dp[i][j][0]:
                            dp[i][j][1] = (dp[i][j][1] + dp[ni][nj][1]) % MOD

        if dp[0][0][0] == NEG_INF:
            return [0, 0]
        return dp[0][0]