class Solution:
    def findRedundantDirectedConnection(self, edges):
        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, rank, x, y):
            rootX, rootY = find(parent, x), find(parent, y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1
                return True
            return False

        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        candidate1 = candidate2 = last = None

        for u, v in edges:
            if parent[v] != v:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
            else:
                parent[v] = u
                if not union(parent, rank, u, v):
                    last = [u, v]

        if candidate1 is None:
            return last
        if last:
            return candidate1
        return candidate2