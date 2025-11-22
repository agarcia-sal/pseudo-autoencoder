from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def count_adjacent_mines(r: int, c: int) -> int:
            mine_count = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'M':
                        mine_count += 1
            return mine_count

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
            if board[r][c] != 'E':
                return

            adjacent_mine_count = count_adjacent_mines(r, c)
            if adjacent_mine_count > 0:
                board[r][c] = str(adjacent_mine_count)
            else:
                board[r][c] = 'B'
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if (i, j) != (r, c):
                            dfs(i, j)

        row, column = click[0], click[1]
        if board[row][column] == 'M':
            board[row][column] = 'X'
            return board

        dfs(row, column)
        return board