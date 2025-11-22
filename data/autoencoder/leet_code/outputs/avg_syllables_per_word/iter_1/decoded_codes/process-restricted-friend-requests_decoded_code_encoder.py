class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)
        if ru != rv:
            if self.size[ru] > self.size[rv]:
                self.parent[rv] = ru
                self.size[ru] += self.size[rv]
            else:
                self.parent[ru] = rv
                self.size[rv] += self.size[ru]

def friendRequests(n, restrictions, requests):
    uf = UnionFind(n)
    res = []
    rmap = {}
    for x, y in restrictions:
        rmap[x] = rmap.get(x, set()) | {y}
        rmap[y] = rmap.get(y, set()) | {x}

    def can_union(u, v):
        ru, rv = uf.find(u), uf.find(v)
        for p in rmap.get(ru, {}):
            if uf.find(p) == rv:
                return False
        for p in rmap.get(rv, {}):
            if uf.find(p) == ru:
                return False
        return True

    for u, v in requests:
        if uf.find(u) == uf.find(v) or can_union(u, v):
            uf.union(u, v)
            res.append(True)
        else:
            res.append(False)
    return res