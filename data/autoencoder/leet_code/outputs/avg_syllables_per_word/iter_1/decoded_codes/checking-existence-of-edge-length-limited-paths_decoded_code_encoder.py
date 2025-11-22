class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rp = self.find(p)
        rq = self.find(q)
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


def distanceLimitedPathsExist(n, edges, queries):
    edges.sort(key=lambda x: x[2])
    qidx = [(lim, p, q, i) for i, (p, q, lim) in enumerate(queries)]
    qidx.sort(key=lambda x: x[0])

    uf = UF(n)
    ei = 0
    res = [False] * len(queries)

    for lim, p, q, i in qidx:
        while ei < len(edges) and edges[ei][2] < lim:
            uf.union(edges[ei][0], edges[ei][1])
            ei += 1
        if uf.find(p) == uf.find(q):
            res[i] = True
    return res