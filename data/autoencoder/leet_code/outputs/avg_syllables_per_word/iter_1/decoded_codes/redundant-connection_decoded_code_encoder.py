class UF:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rp, rq = self.find(p), self.find(q)
        if rp == rq:
            return False
        if self.rank[rp] > self.rank[rq]:
            self.parent[rq] = rp
        elif self.rank[rp] < self.rank[rq]:
            self.parent[rp] = rq
        else:
            self.parent[rq] = rp
            self.rank[rp] += 1
        return True

def findRedundantConnection(edges):
    uf = UF(len(edges) + 1)
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]