class UF:
    def __init__(self):
        self.parent = {}
        self.count = 0

    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.count += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.parent[rx] = ry
            self.count -= 1

def numIslands2(m, n, pos):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    uf = UF()
    grid = [[0]*n for _ in range(m)]
    res = []
    for r, c in pos:
        if grid[r][c] == 1:
            res.append(uf.count)
            continue
        grid[r][c] = 1
        uf.make_set((r, c))
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                uf.union((r, c), (nr, nc))
        res.append(uf.count)
    return res