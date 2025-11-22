class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.count = n

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
            self.count -= 1
            return True
        return False


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        uf_common = UnionFind(n)
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)

        used_edges = 0

        # First, use all type 3 edges
        for t, u, v in edges:
            if t == 3:
                if uf_common.union(u, v):
                    uf_alice.union(u, v)
                    uf_bob.union(u, v)
                    used_edges += 1

        # Use edges for Alice (type 1)
        for t, u, v in edges:
            if t == 1:
                if uf_alice.union(u, v):
                    used_edges += 1

        # Use edges for Bob (type 2)
        for t, u, v in edges:
            if t == 2:
                if uf_bob.union(u, v):
                    used_edges += 1

        if uf_alice.count == 1 and uf_bob.count == 1:
            return len(edges) - used_edges
        else:
            return -1