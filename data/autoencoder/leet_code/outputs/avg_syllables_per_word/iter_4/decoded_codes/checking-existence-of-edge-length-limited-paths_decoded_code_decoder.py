from typing import List, Tuple

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p: int) -> int:
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p: int, q: int) -> bool:
        rootP = self.find(p)
        rootQ = self.find(q)
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
    def distanceLimitedPathsExist(
        self,
        n: int,
        edgeList: List[Tuple[int, int, int]],
        queries: List[Tuple[int, int, int]],
    ) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        indexedQueries = [(limit, p, q, i) for i, (p, q, limit) in enumerate(queries)]
        indexedQueries.sort(key=lambda x: x[0])
        uf = UnionFind(n)
        edgeIndex = 0
        numEdges = len(edgeList)
        results = [False] * len(queries)

        for limit, p, q, originalIndex in indexedQueries:
            while edgeIndex < numEdges and edgeList[edgeIndex][2] < limit:
                u, v, _ = edgeList[edgeIndex]
                uf.union(u, v)
                edgeIndex += 1
            if uf.find(p) == uf.find(q):
                results[originalIndex] = True
        return results