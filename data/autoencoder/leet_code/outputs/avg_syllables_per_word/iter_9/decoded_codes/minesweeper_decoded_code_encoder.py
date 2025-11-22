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

            mines = count_adjacent_mines(r, c)
            if mines > 0:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if i != r or j != c:
                            dfs(i, j)

        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            dfs(r, c)
        return board