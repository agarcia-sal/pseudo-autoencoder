class Solution:
    def areConnected(self, n, threshold, queries):
        if threshold == 0:
            return [True] * len(queries)

        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
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