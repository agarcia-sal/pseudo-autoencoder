from typing import List, Set, Tuple

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
            to_crush: Set[Tuple[int, int]] = set()

            # Check rows for matches
            for r in range(R):
                for c in range(C - 2):
                    v1 = abs(board[r][c])
                    v2 = abs(board[r][c + 1])
                    v3 = abs(board[r][c + 2])
                    if v1 != 0 and v1 == v2 == v3:
                        stable = False
                        to_crush.add((r, c))
                        to_crush.add((r, c + 1))
                        to_crush.add((r, c + 2))

            # Check columns for matches
            for r in range(R - 2):
                for c in range(C):
                    v1 = abs(board[r][c])
                    v2 = abs(board[r + 1][c])
                    v3 = abs(board[r + 2][c])
                    if v1 != 0 and v1 == v2 == v3:
                        stable = False
                        to_crush.add((r, c))
                        to_crush.add((r + 1, c))
                        to_crush.add((r + 2, c))

            # Crush candies
            for r, c in to_crush:
                board[r][c] = 0

            # Drop candies vertically
            for c in range(C):
                wr = R - 1
                for r in range(R - 1, -1, -1):
                    if board[r][c] != 0:
                        board[wr][c] = board[r][c]
                        wr -= 1
                for wr_fill in range(wr, -1, -1):
                    board[wr_fill][c] = 0

        return board