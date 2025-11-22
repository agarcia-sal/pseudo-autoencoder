class Solution:
    def solveNQueens(self, n):
        def is_not_under_attack(row, col):
            return not (cols[col] + hills[row - col] + dales[row + col])

        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hills[row - col] = 1
            dales[row + col] = 1

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hills[row - col] = 0
            dales[row + col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)

        def backtrack(row=0):
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        cols = [0] * n
        hills = [0] * (2 * n - 1)
        dales = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()
        return output