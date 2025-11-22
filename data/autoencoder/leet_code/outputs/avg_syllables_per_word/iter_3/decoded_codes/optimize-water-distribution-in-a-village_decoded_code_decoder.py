class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        for i in range(n):
            pipes.append([0, i + 1, wells[i]])
        pipes.sort(key=lambda x: x[2])
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                return True
            return False

        min_cost = 0
        for h1, h2, cost in pipes:
            if union(h1, h2):
                min_cost += cost
        return min_cost