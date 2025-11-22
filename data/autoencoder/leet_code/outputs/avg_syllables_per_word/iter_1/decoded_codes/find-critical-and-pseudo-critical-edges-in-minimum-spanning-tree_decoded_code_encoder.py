class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)
        if ru != rv:
            if self.rank[ru] > self.rank[rv]:
                self.parent[rv] = ru
            elif self.rank[ru] < self.rank[rv]:
                self.parent[ru] = rv
            else:
                self.parent[rv] = ru
                self.rank[ru] += 1
            return True
        return False


def findCriticalPseudo(n, edges):
    for i, e in enumerate(edges):
        e.append(i)
    edges.sort(key=lambda x: x[2])

    def mst(exclude=None, include=None):
        uf = UF(n)
        w = 0
        if include:
            uf.union(include[0], include[1])
            w += include[2]

        for u, v, wi, idx in edges:
            if idx == exclude:
                continue
            if uf.union(u, v):
                w += wi

        root = uf.find(0)
        for i in range(n):
            if uf.find(i) != root:
                return float('inf')
        return w

    base = mst()
    critical, pseudo = [], []
    for u, v, w, i in edges:
        if mst(exclude=i) > base:
            critical.append(i)
        elif mst(include=(u, v, w)) == base:
            pseudo.append(i)

    return [critical, pseudo]