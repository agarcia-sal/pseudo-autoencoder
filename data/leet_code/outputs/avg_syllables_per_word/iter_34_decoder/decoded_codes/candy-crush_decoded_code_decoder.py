class Solution:
    def candyCrush(self, board):
        R = len(board)
        C = len(board[0])
        stable = False

        while not stable:
            stable = True
            to_crush = set()

            # Check rows for candies to crush
            for r in range(R):
                for c in range(C - 2):
                    val = abs(board[r][c])
                    if val != 0 and val == abs(board[r][c + 1]) == abs(board[r][c + 2]):
                        stable = False
                        to_crush.update({(r, c), (r, c + 1), (r, c + 2)})

            # Check columns for candies to crush
            for r in range(R - 2):
                for c in range(C):
                    val = abs(board[r][c])
                    if val != 0 and val == abs(board[r + 1][c]) == abs(board[r + 2][c]):
                        stable = False
                        to_crush.update({(r, c), (r + 1, c), (r + 2, c)})

            # Set crushed candies to zero
            for r, c in to_crush:
                board[r][c] = 0

            # Apply gravity to let candies fall down
            for c in range(C):
                wr = R - 1
                for r in reversed(range(R)):
                    if board[r][c] != 0:
                        board[wr][c] = board[r][c]
                        wr -= 1
                for i in range(wr, -1, -1):
                    board[i][c] = 0

        return board