from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def count_adjacent_mines(r: int, c: int) -> int:
            count = 0
            for i in range(r - 1, r + 2):
                if 0 <= i < len(board):
                    for j in range(c - 1, c + 2):
                        if 0 <= j < len(board[0]) and board[i][j] == 'M':
                            count += 1
            return count

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
            if board[r][c] != 'E':
                return

            mine_count = count_adjacent_mines(r, c)
            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                board[r][c] = 'B'
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if i == r and j == c:
                            continue
                        dfs(i, j)

        row, col = click[0], click[1]
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board

        dfs(row, col)
        return board