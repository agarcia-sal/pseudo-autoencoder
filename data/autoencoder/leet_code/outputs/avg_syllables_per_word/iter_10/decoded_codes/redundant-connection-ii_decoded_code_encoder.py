class Solution:
    def findRedundantDirectedConnection(self, edges):
        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, rank, x, y):
            rootX = find(parent, x)
            rootY = find(parent, y)
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
        cand1 = None
        cand2 = None
        last = None

        for u, v in edges:
            if parent[v] != v:
                cand1 = [parent[v], v]
                cand2 = [u, v]
            else:
                parent[v] = u
                if not union(parent, rank, u, v):
                    last = [u, v]

        if cand1 is None:
            return last
        if last is not None:
            return cand1
        return cand2