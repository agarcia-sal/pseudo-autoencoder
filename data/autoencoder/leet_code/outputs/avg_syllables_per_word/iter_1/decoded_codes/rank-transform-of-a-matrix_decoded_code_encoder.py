class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def matrixRankTransform(matrix):
    m, n = len(matrix), len(matrix[0])
    value_to_indices = {}

    for r in range(m):
        for c in range(n):
            val = matrix[r][c]
            value_to_indices.setdefault(val, []).append((r, c))

    row_rank = [0] * m
    col_rank = [0] * n
    result = [[0] * n for _ in range(m)]

    for value in sorted(value_to_indices.keys()):
        uf = UnionFind(m + n)
        rank_map = {}

        for r, c in value_to_indices[value]:
            uf.union(r, c + m)

        for r, c in value_to_indices[value]:
            root = uf.find(r)
            rank_map[root] = max(rank_map.get(root, 0), max(row_rank[r], col_rank[c]) + 1)

        for r, c in value_to_indices[value]:
            root = uf.find(r)
            rank = rank_map[root]
            result[r][c] = rank
            row_rank[r] = rank
            col_rank[c] = rank

    return result