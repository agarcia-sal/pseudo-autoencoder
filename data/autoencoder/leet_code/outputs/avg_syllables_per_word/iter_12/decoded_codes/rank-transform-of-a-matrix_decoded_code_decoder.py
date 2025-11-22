from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        # Each element is its own parent initially
        self.parent = list(range(size))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_u] = root_v  # Merge sets

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
            rank = dict()

            # Union rows and columns for the current value
            for r, c in value_to_indices[value]:
                uf.union(r, c + m)

            # Find max rank for each connected component
            for r, c in value_to_indices[value]:
                root = uf.find(r)
                rank[root] = max(rank.get(root, 0), row_rank[r], col_rank[c])

            # Assign ranks and update row_rank and col_rank
            for r, c in value_to_indices[value]:
                root = uf.find(r)
                res_rank = rank[root] + 1
                result[r][c] = res_rank
                row_rank[r] = max(row_rank[r], res_rank)
                col_rank[c] = max(col_rank[c], res_rank)

        return result