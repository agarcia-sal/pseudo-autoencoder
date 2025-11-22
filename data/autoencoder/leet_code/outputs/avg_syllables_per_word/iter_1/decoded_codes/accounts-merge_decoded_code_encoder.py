from collections import defaultdict

class UF:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.rank[rx] > self.rank[ry]:
                self.root[ry] = rx
            elif self.rank[rx] < self.rank[ry]:
                self.root[rx] = ry
            else:
                self.root[ry] = rx
                self.rank[rx] += 1

def accountsMerge(accts):
    uf = UF(len(accts))
    em_to_id = {}
    for i, (n, *emails) in enumerate(accts):
        for e in emails:
            if e not in em_to_id:
                em_to_id[e] = i
            else:
                uf.union(i, em_to_id[e])

    merged = defaultdict(list)
    for e, i in em_to_id.items():
        merged[uf.find(i)].append(e)

    res = []
    for i, emails in merged.items():
        res.append([accts[i][0]] + sorted(emails))
    return res