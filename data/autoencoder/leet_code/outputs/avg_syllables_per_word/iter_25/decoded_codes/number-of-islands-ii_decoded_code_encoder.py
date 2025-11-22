class UnionFind:
    def __init__(self):
        self.parent = {}
        self.count = 0

    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.count += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX
            self.count -= 1


class Solution:
    def numIslands2(self, m, n, positions):
        def is_valid(x, y):
            return 0 <= x < m and 0 <= y < n

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        uf = UnionFind()
        grid = [[0] * n for _ in range(m)]
        result = []

        for r, c in positions:
            if grid[r][c] == 1:
                result.append(uf.count)
                continue

            grid[r][c] = 1
            uf.make_set((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if is_valid(nr, nc) and grid[nr][nc] == 1:
                    uf.union((r, c), (nr, nc))

            result.append(uf.count)

        return result