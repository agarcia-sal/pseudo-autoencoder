from typing import List

class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [0] * n
        hills = [0] * (2 * n - 1)  # "hill" diagonals (row - col + n - 1)
        dales = [0] * (2 * n - 1)  # "dale" diagonals (row + col)

        def is_not_under_attack(row: int, col: int) -> bool:
            # Check if no queen is placed in the current column, hill diagonal, or dale diagonal
            return not (cols[col] + hills[row - col + n - 1] + dales[row + col])

        def place_queen(row: int, col: int) -> None:
            # Mark the column, hill diagonal, and dale diagonal as occupied
            cols[col] = 1
            hills[row - col + n - 1] = 1
            dales[row + col] = 1

        def remove_queen(row: int, col: int) -> None:
            # Remove the queen marking from column, hill diagonal, and dale diagonal
            cols[col] = 0
            hills[row - col + n - 1] = 0
            dales[row + col] = 0

        def backtrack(row: int, count: int) -> int:
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack(row + 1, count)
                    remove_queen(row, col)
            return count

        return backtrack(0, 0)