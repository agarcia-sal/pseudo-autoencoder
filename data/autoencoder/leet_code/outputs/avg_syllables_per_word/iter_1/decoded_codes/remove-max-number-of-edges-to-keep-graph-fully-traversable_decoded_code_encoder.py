class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        self.count -= 1
        return True


def max_num_edges_to_remove(n, edges):
    uf_common = UnionFind(n)
    uf_alice = UnionFind(n)
    uf_bob = UnionFind(n)
    used = 0

    for t, u, v in edges:
        u -= 1
        v -= 1
        if t == 3 and uf_common.union(u, v):
            uf_alice.union(u, v)
            uf_bob.union(u, v)
            used += 1

    for t, u, v in edges:
        u -= 1
        v -= 1
        if t == 1 and uf_alice.union(u, v):
            used += 1
        elif t == 2 and uf_bob.union(u, v):
            used += 1

    if uf_alice.count == 1 and uf_bob.count == 1:
        return len(edges) - used
    return -1