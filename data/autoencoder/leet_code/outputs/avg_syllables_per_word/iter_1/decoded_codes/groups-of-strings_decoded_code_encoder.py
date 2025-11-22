from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, u):
        while self.parent[u] != u:
            self.parent[u] = self.parent[self.parent[u]]
            u = self.parent[u]
        return u

    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)
        if ru != rv:
            if self.rank[ru] > self.rank[rv]:
                self.parent[rv] = ru
                self.size[ru] += self.size[rv]
            elif self.rank[ru] < self.rank[rv]:
                self.parent[ru] = rv
                self.size[rv] += self.size[ru]
            else:
                self.parent[rv] = ru
                self.size[ru] += self.size[rv]
                self.rank[ru] += 1


def bitmask(w):
    m = 0
    for c in w:
        m |= 1 << (ord(c) - ord('a'))
    return m


def groupStrings(words):
    n = len(words)
    uf = UnionFind(n)
    wm = defaultdict(list)  # bitmask -> indices

    for i, w in enumerate(words):
        wm[bitmask(w)].append(i)

    for i, w in enumerate(words):
        m = bitmask(w)
        for j in range(26):
            # delete letter j
            nm = m ^ (1 << j)
            if nm in wm:
                for k in wm[nm]:
                    uf.union(i, k)

            # add letter j
            if (m & (1 << j)) == 0:
                nm = m | (1 << j)
                if nm in wm:
                    for k in wm[nm]:
                        uf.union(i, k)

            # replace letter j with k
            if m & (1 << j):
                for k in range(26):
                    if (m & (1 << k)) == 0:
                        nm = (m ^ (1 << j)) | (1 << k)
                        if nm in wm:
                            for l in wm[nm]:
                                uf.union(i, l)

    roots = defaultdict(int)
    for i in range(n):
        roots[uf.find(i)] += 1

    return [len(roots), max(roots.values())]