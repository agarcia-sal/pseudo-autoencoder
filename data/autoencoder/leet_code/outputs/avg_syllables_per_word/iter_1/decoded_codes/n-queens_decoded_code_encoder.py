def solveNQueens(n):
    cols = [0]*n
    hills = [0]*(2*n-1)     # "hill" diagonals
    dales = [0]*(2*n-1)     # "dale" diagonals
    queens = set()
    output = []

    def is_safe(r, c):
        return not (cols[c] or hills[r - c + n - 1] or dales[r + c])

    def place(r, c):
        queens.add((r, c))
        cols[c] = 1
        hills[r - c + n - 1] = 1
        dales[r + c] = 1

    def remove(r, c):
        queens.remove((r, c))
        cols[c] = 0
        hills[r - c + n - 1] = 0
        dales[r + c] = 0

    def add_solution():
        solution = []
        for _, c in sorted(queens):
            solution.append("." * c + "Q" + "." * (n - c - 1))
        output.append(solution)

    def backtrack(r=0):
        for c in range(n):
            if is_safe(r, c):
                place(r, c)
                if r + 1 == n:
                    add_solution()
                else:
                    backtrack(r + 1)
                remove(r, c)

    backtrack()
    return output