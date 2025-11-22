class Solution:
    def updateBoard(self, board, click):
        mine_indicator = 'M'
        unrevealed_indicator = 'E'
        explosion_indicator = 'X'
        blank_indicator = 'B'

        rows, cols = len(board), len(board[0])

        def count_adjacent_mines(row, col):
            mine_count = 0
            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if 0 <= i < rows and 0 <= j < cols:
                        if board[i][j] == mine_indicator:
                            mine_count += 1
            return mine_count

        def dfs(row, col):
            if not (0 <= row < rows and 0 <= col < cols):
                return
            if board[row][col] != unrevealed_indicator:
                return

            adjacent_mines = count_adjacent_mines(row, col)
            if adjacent_mines > 0:
                board[row][col] = str(adjacent_mines)
            else:
                board[row][col] = blank_indicator
                for i in range(row - 1, row + 2):
                    for j in range(col - 1, col + 2):
                        if i == row and j == col:
                            continue  # Already processed current cell
                        dfs(i, j)

        row, col = click
        if board[row][col] == mine_indicator:
            board[row][col] = explosion_indicator
            return board

        dfs(row, col)
        return board