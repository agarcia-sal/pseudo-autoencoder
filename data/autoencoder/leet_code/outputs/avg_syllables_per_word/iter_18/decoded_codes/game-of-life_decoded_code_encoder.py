from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in (1, 3):
                        live_neighbors += 1

                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 3  # live -> dead
                else:
                    if live_neighbors == 3:
                        board[i][j] = 2  # dead -> live

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0