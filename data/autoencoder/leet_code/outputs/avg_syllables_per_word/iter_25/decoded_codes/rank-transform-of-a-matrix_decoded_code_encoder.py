from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_u] = root_v

class Solution:
    def matrixRankTransform(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0

        value_to_indices = defaultdict(list)
        for r in range(m):
            for c in range(n):
                value_to_indices[matrix[r][c]].append((r, c))

        row_rank = [0] * m
        col_rank = [0] * n
        result = [[0] * n for _ in range(m)]

        for value in sorted(value_to_indices.keys()):
            uf = UnionFind(m + n)
            rank = {}

            # Union rows and columns connected by the same value
            for r, c in value_to_indices[value]:
                uf.union(r, c + m)

            # Compute the rank for each connected component root
            for r, c in value_to_indices[value]:
                root = uf.find(r)
                rank[root] = max(rank.get(root, 0), max(row_rank[r], col_rank[c]) + 1)

            # Assign ranks and update row_rank and col_rank
            for r, c in value_to_indices[value]:
                root = uf.find(r)
                val_rank = rank[root]
                result[r][c] = val_rank
                row_rank[r] = val_rank
                col_rank[c] = val_rank

        return result