from typing import List, Optional
import math

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
    def findCriticalAndPseudoCriticalEdges(
        self,
        n: int,
        edges: List[List[int]],
    ) -> List[List[int]]:

        # Append original index to each edge for identification
        for i, edge in enumerate(edges):
            edge.append(i)

        # Sort edges by weight (element at position 2)
        edges.sort(key=lambda x: x[2])

        def mst(exclude: Optional[int] = None, include: Optional[List[int]] = None) -> float:
            uf = UnionFind(n)
            weight = 0

            if include is not None:
                included_u, included_v, included_w, _ = include
                # Force include this edge
                uf.union(included_u, included_v)
                weight += included_w

            for u, v, w, idx in edges:
                if idx == exclude:
                    continue
                if uf.union(u, v):
                    weight += w

            root = uf.find(0)
            for i in range(n):
                if uf.find(i) != root:
                    return math.inf
            return weight

        mst_weight = mst()

        critical = []
        pseudo_critical = []

        for u, v, w, idx in edges:
            # Check if edge is critical
            if mst(exclude=idx) > mst_weight:
                critical.append(idx)
            # Check if edge is pseudo-critical
            elif mst(include=[u, v, w, idx]) == mst_weight:
                pseudo_critical.append(idx)

        return [critical, pseudo_critical]