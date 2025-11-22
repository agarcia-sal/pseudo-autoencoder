class Solution:
    def areConnected(self, n: int, threshold: int, queries: list[list[int]]) -> list[bool]:
        if threshold == 0:
            return [True] * len(queries)

        parent = list(range(n + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        for i in range(threshold + 1, n + 1):
            for j in range(2 * i, n + 1, i):
                union(i, j)

        result = []
        for a, b in queries:
            result.append(find(a) == find(b))

        return result