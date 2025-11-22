from typing import List, Tuple

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[Tuple[int, int]]) -> List[bool]:
        if threshold == 0:
            return [True] * len(queries)

        parent = list(range(n + 1))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        for i in range(threshold + 1, n + 1):
            for j in range(i * 2, n + 1, i):
                union(i, j)

        result = []
        for a, b in queries:
            result.append(find(a) == find(b))

        return result