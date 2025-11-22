def updateBoard(board, click):
    def countMines(r, c):
        return sum(0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'M'
                   for i in range(r-1, r+2) for j in range(c-1, c+2))

    def dfs(r, c):
        if not (0 <= r < len(board) and 0 <= c < len(board[0])) or board[r][c] != 'E':
            return
        m = countMines(r, c)
        board[r][c] = str(m) if m > 0 else 'B'
        if m == 0:
            for i in range(r-1, r+2):
                for j in range(c, c+2):
                    dfs(i, j)

    r, c = click
    if board[r][c] == 'M':
        board[r][c] = 'X'
        return board
    dfs(r, c)
    return board