from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])

        def dfs(x: int, y: int) -> None:
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
                return
            board[x][y] = 'S'
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'S':
                    board[i][j] = 'O'