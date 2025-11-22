def total_n_queens(n):
    cols = [0] * n
    hills = [0] * (2 * n - 1)  # r - c + n - 1 shifted to 0..2n-2
    dales = [0] * (2 * n - 1)  # r + c

    def is_safe(r, c):
        return cols[c] + hills[r - c + n - 1] + dales[r + c] == 0

    def place(r, c):
        cols[c] = 1
        hills[r - c + n - 1] = 1
        dales[r + c] = 1

    def remove(r, c):
        cols[c] = 0
        hills[r - c + n - 1] = 0
        dales[r + c] = 0

    def backtrack(r=0, cnt=0):
        for c in range(n):
            if is_safe(r, c):
                place(r, c)
                if r + 1 == n:
                    cnt += 1
                else:
                    cnt = backtrack(r + 1, cnt)
                remove(r, c)
        return cnt

    return backtrack()