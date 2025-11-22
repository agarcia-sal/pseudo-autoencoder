from typing import List

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R = len(board)
        C = len(board[0]) if R > 0 else 0
        stable = False

        while not stable:
            stable = True
            to_crush = set()

            # Check rows for crush
            for r in range(R):
                for c in range(C - 2):
                    v = abs(board[r][c])
                    if v != 0 and v == abs(board[r][c + 1]) == abs(board[r][c + 2]):
                        stable = False
                        to_crush.add((r, c))
                        to_crush.add((r, c + 1))
                        to_crush.add((r, c + 2))

            # Check columns for crush
            for r in range(R - 2):
                for c in range(C):
                    v = abs(board[r][c])
                    if v != 0 and v == abs(board[r + 1][c]) == abs(board[r + 2][c]):
                        stable = False
                        to_crush.add((r, c))
                        to_crush.add((r + 1, c))
                        to_crush.add((r + 2, c))

            # Set the crush positions to zero
            for r, c in to_crush:
                board[r][c] = 0

            # Drop the candies
            for c in range(C):
                wr = R - 1
                for r in range(R - 1, -1, -1):
                    if board[r][c] != 0:
                        board[wr][c] = board[r][c]
                        wr -= 1
                for wr2 in range(wr, -1, -1):
                    board[wr2][c] = 0

        return board