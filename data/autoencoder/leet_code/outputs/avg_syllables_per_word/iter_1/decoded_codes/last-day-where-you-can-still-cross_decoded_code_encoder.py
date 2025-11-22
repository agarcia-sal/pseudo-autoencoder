class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.r[rx] > self.r[ry]:
                self.p[ry] = rx
            elif self.r[rx] < self.r[ry]:
                self.p[rx] = ry
            else:
                self.p[ry] = rx
                self.r[rx] += 1

def latestDayToCross(row, col, cells):
    grid = [[1] * col for _ in range(row)]
    uf = UF(row * col + 2)
    TOP, BOTTOM = row * col, row * col + 1
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for day in range(len(cells) - 1, -1, -1):
        r, c = cells[day][0] - 1, cells[day][1] - 1
        grid[r][c] = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                uf.union(r * col + c, nr * col + nc)
        if r == 0:
            uf.union(r * col + c, TOP)
        if r == row - 1:
            uf.union(r * col + c, BOTTOM)
        if uf.find(TOP) == uf.find(BOTTOM):
            return day

    return 0