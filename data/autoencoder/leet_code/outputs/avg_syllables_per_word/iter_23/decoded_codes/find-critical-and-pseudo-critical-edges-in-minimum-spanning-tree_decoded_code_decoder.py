from typing import List, Optional, Tuple

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> bool:
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
            return True
        return False


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Append original indices to edges for tracking after sorting
        for i, edge in enumerate(edges):
            edge.append(i)

        edges.sort(key=lambda x: x[2])  # sort by weight ascending

        def mst(exclude: Optional[int] = None, include: Optional[Tuple[int, int, int]] = None) -> int:
            uf = UnionFind(n)
            total_weight = 0

            # If an edge is included forcibly, do it first
            if include is not None:
                u, v, w = include
                uf.union(u, v)
                total_weight += w

            for u, v, w, idx in edges:
                if idx == exclude:
                    continue
                if uf.union(u, v):
                    total_weight += w

            root = uf.find(0)
            for i in range(n):
                if uf.find(i) != root:
                    return float('inf')
            return total_weight

        mst_weight = mst()

        critical = []
        pseudo_critical = []

        for u, v, w, idx in edges:
            # Check if excluding edge idx increases MST weight
            if mst(exclude=idx) > mst_weight:
                critical.append(idx)
            else:
                # Check if including edge idx keeps MST weight the same
                if mst(include=(u, v, w)) == mst_weight:
                    pseudo_critical.append(idx)

        return [critical, pseudo_critical]