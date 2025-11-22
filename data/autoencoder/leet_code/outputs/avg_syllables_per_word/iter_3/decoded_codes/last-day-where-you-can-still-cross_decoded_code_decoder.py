class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def latestDayToCross(self, row, col, cells):
        grid = [[1]*col for _ in range(row)]
        uf = UnionFind(row * col + 2)
        TOP, BOTTOM = row * col, row * col + 1
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        for day in range(len(cells)-1, -1, -1):
            r, c = cells[day]
            r -= 1
            c -= 1
            grid[r][c] = 0
            idx = r * col + c

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                    uf.union(idx, nr * col + nc)

            if r == 0:
                uf.union(idx, TOP)
            if r == row - 1:
                uf.union(idx, BOTTOM)

            if uf.find(TOP) == uf.find(BOTTOM):
                return day
        return 0