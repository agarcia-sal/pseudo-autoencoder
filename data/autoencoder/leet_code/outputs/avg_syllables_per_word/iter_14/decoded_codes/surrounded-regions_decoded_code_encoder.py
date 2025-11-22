class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
                return
            board[x][y] = 'S'  # mark safe 'O's connected to borders
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        # Start DFS from 'O's on the borders
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        # Flip all remaining 'O's to 'X's
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        # Flip back all 'S's to 'O's
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'S':
                    board[i][j] = 'O'