def gameOfLife(board):
    if not board or not board[0]:
        return

    m, n = len(board), len(board[0])
    dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    for i in range(m):
        for j in range(n):
            cnt = 0
            for dx, dy in dirs:
                ni, nj = i + dx, j + dy
                if 0 <= ni < m and 0 <= nj < n:
                    if board[ni][nj] in {1, 3}:
                        cnt += 1

            if board[i][j] == 1 and (cnt < 2 or cnt > 3):
                board[i][j] = 3
            if board[i][j] == 0 and cnt == 3:
                board[i][j] = 2

    for i in range(m):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 1
            elif board[i][j] == 3:
                board[i][j] = 0