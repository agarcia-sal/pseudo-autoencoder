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

        candidate1 = None
        candidate2 = None
        last = None

        # To detect if a node has two parents
        parent_map = list(range(n + 1))

        for u, v in edges:
            if parent_map[v] != v:
                candidate1 = [parent_map[v], v]
                candidate2 = [u, v]
            else:
                parent_map[v] = u

        # Reset DSU structures for union find after checking two parents condition
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        for u, v in edges:
            # If there is a candidate2 edge, skip it temporarily to check if cycle occurs without it
            if candidate2 is not None and [u, v] == candidate2:
                continue
            if not union(parent, rank, u, v):
                last = [u, v]

        if candidate1 is None:
            return last
        if last is not None:
            return candidate1
        return candidate2