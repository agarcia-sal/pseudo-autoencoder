from typing import List, Set, Tuple

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R = len(board)
        C = len(board[0]) if R > 0 else 0
        stable = False

        while not stable:
            stable = True
            to_crush: Set[Tuple[int, int]] = set()

            # Check rows for candies to crush
            for r in range(R):
                for c in range(C - 2):
                    val = abs(board[r][c])
                    if val != 0 and val == abs(board[r][c + 1]) == abs(board[r][c + 2]):
                        stable = False
                        to_crush.add((r, c))
                        to_crush.add((r, c + 1))
                        to_crush.add((r, c + 2))

            # Check columns for candies to crush
            for r in range(R - 2):
                for c in range(C):
                    val = abs(board[r][c])
                    if val != 0 and val == abs(board[r + 1][c]) == abs(board[r + 2][c]):
                        stable = False
                        to_crush.add((r, c))
                        to_crush.add((r + 1, c))
                        to_crush.add((r + 2, c))

            # Crush the candies
            for r, c in to_crush:
                board[r][c] = 0

            # Drop candies
            for c in range(C):
                wr = R - 1  # Write row pointer
                for r in range(R - 1, -1, -1):
                    if board[r][c] != 0:
                        board[wr][c] = board[r][c]
                        wr -= 1
                for r in range(wr, -1, -1):
                    board[r][c] = 0

        return board