class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def is_not_under_attack(row: int, col: int) -> bool:
            return not (cols[col] + hills[row - col] + dales[row + col])

        def place_queen(row: int, col: int) -> None:
            queens.add((row, col))
            cols[col] = 1
            hills[row - col] = 1
            dales[row + col] = 1

        def remove_queen(row: int, col: int) -> None:
            queens.remove((row, col))
            cols[col] = 0
            hills[row - col] = 0
            dales[row + col] = 0

        def add_solution() -> None:
            solution = []
            for _, col in sorted(queens):
                line = "." * col + "Q" + "." * (n - col - 1)
                solution.append(line)
            output.append(solution)

        def backtrack(row: int = 0) -> None:
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        cols = [0] * n
        # adjust hills and dales indexing to avoid negative indices
        hills = [0] * (2 * n - 1)
        dales = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()
        return output