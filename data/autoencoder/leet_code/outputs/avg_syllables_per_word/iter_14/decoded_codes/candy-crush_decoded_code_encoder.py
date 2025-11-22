class Solution:
    def candyCrush(self, board):
        R, C = len(board), len(board[0])
        stable = False

        while not stable:
            stable = True
            to_crush = set()

            # Check rows for crush
            for r in range(R):
                for c in range(C - 2):
                    val = abs(board[r][c])
                    if val != 0 and val == abs(board[r][c+1]) == abs(board[r][c+2]):
                        stable = False
                        to_crush.update({(r, c), (r, c+1), (r, c+2)})

            # Check columns for crush
            for r in range(R - 2):
                for c in range(C):
                    val = abs(board[r][c])
                    if val != 0 and val == abs(board[r+1][c]) == abs(board[r+2][c]):
                        stable = False
                        to_crush.update({(r, c), (r+1, c), (r+2, c)})

            # Set crushed positions to zero
            for r, c in to_crush:
                board[r][c] = 0

            # Apply gravity
            for c in range(C):
                wr = R - 1
                for r in range(R - 1, -1, -1):
                    if board[r][c] != 0:
                        board[wr][c] = board[r][c]
                        wr -= 1
                for r in range(wr, -1, -1):
                    board[r][c] = 0

        return board