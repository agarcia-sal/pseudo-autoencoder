class Solution:
    def updateBoard(self, board, click):
        def count_adjacent_mines(row, column):
            mine_count = 0
            for i in range(row - 1, row + 2):
                for j in range(column - 1, column + 2):
                    if (
                        0 <= i < len(board) and
                        0 <= j < len(board[0]) and
                        board[i][j] == 'M'
                    ):
                        mine_count += 1
            return mine_count

        def dfs(row, column):
            if not (0 <= row < len(board) and 0 <= column < len(board[0])):
                return
            if board[row][column] != 'E':
                return

            adjacent_mines = count_adjacent_mines(row, column)
            if adjacent_mines > 0:
                board[row][column] = str(adjacent_mines)
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