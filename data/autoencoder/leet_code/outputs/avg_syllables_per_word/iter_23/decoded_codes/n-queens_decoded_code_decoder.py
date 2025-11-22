class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        cols = [0] * n
        hills = [0] * (2 * n - 1)  # "hill" diagonals: row - col + (n - 1)
        dales = [0] * (2 * n - 1)  # "dale" diagonals: row + col
        queens = set()
        output = []

        def is_not_under_attack(row: int, col: int) -> bool:
            return not (cols[col] == 1 or hills[row - col + n - 1] == 1 or dales[row + col] == 1)

        def place_queen(row: int, col: int) -> None:
            queens.add((row, col))
            cols[col] = 1
            hills[row - col + n - 1] = 1
            dales[row + col] = 1

        def remove_queen(row: int, col: int) -> None:
            queens.remove((row, col))
            cols[col] = 0
            hills[row - col + n - 1] = 0
            dales[row + col] = 0

        def add_solution() -> None:
            solution = []
            for queen_row, queen_col in sorted(queens):
                position_string = '.' * queen_col + 'Q' + '.' * (n - queen_col - 1)
                solution.append(position_string)
            output.append(solution)

        def backtrack(row: int) -> None:
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        backtrack(0)
        return output