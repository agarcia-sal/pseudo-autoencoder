from typing import List

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_common = UnionFind(n)
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)

        used_edges = 0

        # Type 3 edges: shared by Alice and Bob, union in all three uf
        for t, u, v in edges:
            u -= 1  # zero-based index
            v -= 1
            if t == 3:
                if uf_common.union(u, v):
                    uf_alice.union(u, v)
                    uf_bob.union(u, v)
                    used_edges += 1

        # Type 1 edges: Alice only
        for t, u, v in edges:
            u -= 1
            v -= 1
            if t == 1:
                if uf_alice.union(u, v):
                    used_edges += 1

        # Type 2 edges: Bob only
        for t, u, v in edges:
            u -= 1
            v -= 1
            if t == 2:
                if uf_bob.union(u, v):
                    used_edges += 1

        # Check if both fully connected
        if uf_alice.count == 1 and uf_bob.count == 1:
            return len(edges) - used_edges
        return -1