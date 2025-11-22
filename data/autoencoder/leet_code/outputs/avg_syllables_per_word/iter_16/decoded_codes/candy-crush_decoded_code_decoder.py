class Solution:
    def candyCrush(self, board):
        R = len(board)
        C = len(board[0]) if board else 0
        stable = False

        while not stable:
            stable = True
            to_crush = set()

            # Check rows for triples
            for r in range(R):
                for c in range(C - 2):
                    val = abs(board[r][c])
                    if val != 0 and val == abs(board[r][c + 1]) == abs(board[r][c + 2]):
                        stable = False
                        to_crush.add((r, c))
                        to_crush.add((r, c + 1))
                        to_crush.add((r, c + 2))

            # Check columns for triples
            for r in range(R - 2):
                for c in range(C):
                    val = abs(board[r][c])
                    if val != 0 and val == abs(board[r + 1][c]) == abs(board[r + 2][c]):
                        stable = False
                        to_crush.add((r, c))
                        to_crush.add((r + 1, c))
                        to_crush.add((r + 2, c))

            # Crush marked positions
            for r, c in to_crush:
                board[r][c] = 0

            # Drop candies
            for c in range(C):
                wr = R - 1
                for r in range(R - 1, -1, -1):
                    if board[r][c] != 0:
                        board[wr][c] = board[r][c]
                        wr -= 1
                for fill_r in range(wr, -1, -1):
                    board[fill_r][c] = 0

        return board