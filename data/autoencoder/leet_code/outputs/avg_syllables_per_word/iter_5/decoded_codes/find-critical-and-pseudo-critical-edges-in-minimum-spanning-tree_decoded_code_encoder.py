class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU, rootV = self.find(u), self.find(v)
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
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        for i, edge in enumerate(edges):
            edge.append(i)

        edges.sort(key=lambda x: x[2])

        def mst(exclude=None, include=None):
            uf = UnionFind(n)
            weight = 0
            if include:
                uf.union(include[0], include[1])
                weight += include[2]
            for u, v, w, idx in edges:
                if idx == exclude:
                    continue
                if uf.union(u, v):
                    weight += w
            root = uf.find(0)
            for i in range(n):
                if uf.find(i) != root:
                    return float('inf')
            return weight

        mst_weight = mst()

        critical = []
        pseudo_critical = []

        for u, v, w, idx in edges:
            if mst(exclude=idx) > mst_weight:
                critical.append(idx)
            elif mst(include=(u, v, w)) == mst_weight:
                pseudo_critical.append(idx)

        return [critical, pseudo_critical]