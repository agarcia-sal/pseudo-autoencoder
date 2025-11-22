from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        MINE = 'M'
        EMPTY = 'E'
        BLANK = 'B'
        EXPLODED = 'X'

        rows, cols = len(board), len(board[0]) if board else 0

        def count_adjacent_mines(r: int, c: int) -> int:
            count = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if 0 <= i < rows and 0 <= j < cols and board[i][j] == MINE:
                        count += 1
            return count

        def dfs(r: int, c: int):
            if not (0 <= r < rows and 0 <= c < cols):
                return
            if board[r][c] != EMPTY:
                return

            mine_count = count_adjacent_mines(r, c)
            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                board[r][c] = BLANK
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        dfs(i, j)

        row, col = click
        if board[row][col] == MINE:
            board[row][col] = EXPLODED
            return board

        dfs(row, col)
        return board