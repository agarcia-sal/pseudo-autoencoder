from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def count_adjacent_mines(row: int, column: int) -> int:
            count = 0
            for i in range(row - 1, row + 2):
                for j in range(column - 1, column + 2):
                    if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'M':
                        count += 1
            return count

        def dfs(row: int, column: int) -> None:
            if not (0 <= row < len(board) and 0 <= column < len(board[0])):
                return
            if board[row][column] != 'E':
                return

            mine_count = count_adjacent_mines(row, column)
            if mine_count > 0:
                board[row][column] = str(mine_count)
            else:
                board[row][column] = 'B'
                for i in range(row - 1, row + 2):
                    for j in range(column - 1, column + 2):
                        dfs(i, j)

        row, col = click[0], click[1]
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board

        dfs(row, col)
        return board