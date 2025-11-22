from typing import List

class UnionFind:
    def __init__(self, n: int):
        # parent[i] = parent of node i; initially each node is its own parent
        self.parent = list(range(n + 1))
        # rank[i] is used to keep tree short
        self.rank = [0] * (n + 1)
        # count of connected components
        self.count = n

    def find(self, u: int) -> int:
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
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

        # First, process all type 3 edges (common)
        for t, u, v in edges:
            if t == 3:
                if uf_common.union(u, v):
                    uf_alice.union(u, v)
                    uf_bob.union(u, v)
                    used_edges += 1

        # Process type 1 edges (Alice only)
        for t, u, v in edges:
            if t == 1:
                if uf_alice.union(u, v):
                    used_edges += 1

        # Process type 2 edges (Bob only)
        for t, u, v in edges:
            if t == 2:
                if uf_bob.union(u, v):
                    used_edges += 1

        # Check if both Alice and Bob can traverse the entire graph (1 connected component)
        if uf_alice.count == 1 and uf_bob.count == 1:
            return len(edges) - used_edges
        else:
            return -1