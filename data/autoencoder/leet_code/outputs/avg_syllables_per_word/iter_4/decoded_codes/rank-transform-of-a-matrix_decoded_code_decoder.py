from collections import defaultdict

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> None:
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_u] = root_v

class Solution:
    def matrixRankTransform(self, matrix: list[list[int]]) -> list[list[int]]:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        value_to_indices = defaultdict(list)
        for r in range(m):
            for c in range(n):
                value_to_indices[matrix[r][c]].append((r, c))

        row_rank = [0] * m
        col_rank = [0] * n
        result = [[0] * n for _ in range(m)]

        for value in sorted(value_to_indices):
            uf = UnionFind(m + n)
            for r, c in value_to_indices[value]:
                uf.union(r, c + m)

            rank = dict()
            for r, c in value_to_indices[value]:
                root = uf.find(r)
                prev = rank.get(root, 0)
                rank[root] = max(prev, max(row_rank[r], col_rank[c]) + 1)

            for r, c in value_to_indices[value]:
                root = uf.find(r)
                res_rank = rank[root]
                result[r][c] = res_rank
                row_rank[r] = res_rank
                col_rank[c] = res_rank

        return result