from typing import List

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R = len(board)
        if R == 0:
            return board
        C = len(board[0])
        if C == 0:
            return board

        stable = False

        while not stable:
            stable = True
            to_crush = set()

            # Check horizontal triples
            for r in range(R):
                for c in range(C - 2):
                    val0 = abs(board[r][c])
                    val1 = abs(board[r][c + 1])
                    val2 = abs(board[r][c + 2])
                    if val0 != 0 and val0 == val1 and val1 == val2:
                        stable = False
                        to_crush.add((r, c))
                        to_crush.add((r, c + 1))
                        to_crush.add((r, c + 2))

            # Check vertical triples
            for r in range(R - 2):
                for c in range(C):
                    val0 = abs(board[r][c])
                    val1 = abs(board[r + 1][c])
                    val2 = abs(board[r + 2][c])
                    if val0 != 0 and val0 == val1 and val1 == val2:
                        stable = False
                        to_crush.add((r, c))
                        to_crush.add((r + 1, c))
                        to_crush.add((r + 2, c))

            # Mark to crush
            for r, c in to_crush:
                board[r][c] = 0

            # Drop row-wise for each column
            for c in range(C):
                wr = R - 1  # write pointer
                for r in range(R - 1, -1, -1):
                    if board[r][c] != 0:
                        board[wr][c] = board[r][c]
                        wr -= 1
                for rr in range(wr, -1, -1):
                    board[rr][c] = 0

        return board