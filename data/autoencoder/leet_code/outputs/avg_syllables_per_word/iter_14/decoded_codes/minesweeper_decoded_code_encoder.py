class Solution:
    def updateBoard(self, board, click):
        MINE = 'M'
        EMPTY = 'E'
        BLANK = 'B'
        EXPLODED = 'X'

        def count_adjacent_mines(r, c):
            count = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if 0 <= i < len(board) and 0 <= j < len(board[0]):
                        if board[i][j] == MINE:
                            count += 1
            return count

        def dfs(r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
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

        row, col = click[0], click[1]
        if board[row][col] == MINE:
            board[row][col] = EXPLODED
            return board

        dfs(row, col)
        return board