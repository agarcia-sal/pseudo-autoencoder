class Solution:
    def candyCrush(self, board: list[list[int]]) -> list[list[int]]:
        R = len(board)
        if R == 0:
            return board
        C = len(board[0])
        stable = False

        while not stable:
            stable = True
            to_crush = set()

            # Check rows for crushes
            for r in range(R):
                for c in range(C - 2):
                    v0 = abs(board[r][c])
                    v1 = abs(board[r][c + 1])
                    v2 = abs(board[r][c + 2])
                    if v0 != 0 and v0 == v1 == v2:
                        stable = False
                        to_crush.add((r, c))
                        to_crush.add((r, c + 1))
                        to_crush.add((r, c + 2))

            # Check columns for crushes
            for r in range(R - 2):
                for c in range(C):
                    v0 = abs(board[r][c])
                    v1 = abs(board[r + 1][c])
                    v2 = abs(board[r + 2][c])
                    if v0 != 0 and v0 == v1 == v2:
                        stable = False
                        to_crush.add((r, c))
                        to_crush.add((r + 1, c))
                        to_crush.add((r + 2, c))

            # Set crushed positions to zero
            for r, c in to_crush:
                board[r][c] = 0

            # Drop candies
            for c in range(C):
                wr = R - 1
                for r in range(R - 1, -1, -1):
                    if board[r][c] != 0:
                        board[wr][c] = board[r][c]
                        if wr != r:
                            board[r][c] = 0
                        wr -= 1
                for fill_r in range(wr, -1, -1):
                    board[fill_r][c] = 0

        return board