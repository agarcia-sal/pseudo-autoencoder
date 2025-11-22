class Solution:
    def updateBoard(self, board, click):
        rows, cols = len(board), len(board[0])

        def count_adjacent_mines(r, c):
            count = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if 0 <= i < rows and 0 <= j < cols and board[i][j] == 'M':
                        count += 1
            return count

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != 'E':
                return
            mine_count = count_adjacent_mines(r, c)
            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                board[r][c] = 'B'
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if (i, j) != (r, c):
                            dfs(i, j)

        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board

        dfs(row, col)
        return board