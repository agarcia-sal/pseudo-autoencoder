class Solution:
    def gameOfLife(self, board) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        for r in range(rows):
            for c in range(cols):
                live_neighbors = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (board[nr][nc] == 1 or board[nr][nc] == 3):
                        live_neighbors += 1

                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 3  # alive->dead
                else:
                    if live_neighbors == 3:
                        board[r][c] = 2  # dead->alive

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == 3:
                    board[r][c] = 0