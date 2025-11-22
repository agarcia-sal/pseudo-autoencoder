from typing import List, Set, Tuple

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols: List[int] = [0] * n
        hills: List[int] = [0] * (2 * n - 1)
        dales: List[int] = [0] * (2 * n - 1)
        queens: Set[Tuple[int, int]] = set()
        output: List[List[str]] = []

        def is_not_under_attack(row: int, col: int) -> bool:
            # Check if the position is not attacked by any queen already placed
            return not (cols[col] == 1 or hills[row - col] == 1 or dales[row + col] == 1)

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
            solution: List[str] = []
            for r, c in sorted(queens, key=lambda x: x[0]):
                line_prefix = '.' * c
                line_suffix = '.' * (n - c - 1)
                line = line_prefix + 'Q' + line_suffix
                solution.append(line)
            output.append(solution)

        def backtrack(row: int = 0) -> None:
            if row == n:
                add_solution()
                return
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    backtrack(row + 1)
                    remove_queen(row, col)

        backtrack()
        return output