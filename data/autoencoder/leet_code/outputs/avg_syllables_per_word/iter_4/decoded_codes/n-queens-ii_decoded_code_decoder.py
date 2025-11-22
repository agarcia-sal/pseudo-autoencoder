class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = [0] * n
        hills = [0] * (2 * n - 1)  # "hill" diagonals
        dales = [0] * (2 * n - 1)  # "dale" diagonals

        def is_not_under_attack(row: int, col: int) -> bool:
            return not (cols[col] or hills[row - col] or dales[row + col])

        def place_queen(row: int, col: int) -> None:
            cols[col] = 1
            hills[row - col] = 1
            dales[row + col] = 1

        def remove_queen(row: int, col: int) -> None:
            cols[col] = 0
            hills[row - col] = 0
            dales[row + col] = 0

        def backtrack(row: int = 0, count: int = 0) -> int:
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack(row + 1, count)
                    remove_queen(row, col)
            return count

        return backtrack()