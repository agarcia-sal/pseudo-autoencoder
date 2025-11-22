class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        while self.parent[p] != p:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, p, q):
        rootP, rootQ = self.find(p), self.find(q)
        if rootP == rootQ:
            return False
        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1
        return True


class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries):
        edgeList.sort(key=lambda x: x[2])
        indexedQueries = sorted(
            [(limit, p, q, i) for i, (p, q, limit) in enumerate(queries)],
            key=lambda x: x[0]
        )
        uf = UnionFind(n)
        edgeIndex = 0
        numEdges = len(edgeList)
        results = [False] * len(queries)

        for limit, p, q, qi in indexedQueries:
            while edgeIndex < numEdges and edgeList[edgeIndex][2] < limit:
                u, v = edgeList[edgeIndex][0], edgeList[edgeIndex][1]
                uf.union(u, v)
                edgeIndex += 1
            if uf.find(p) == uf.find(q):
                results[qi] = True

        return results