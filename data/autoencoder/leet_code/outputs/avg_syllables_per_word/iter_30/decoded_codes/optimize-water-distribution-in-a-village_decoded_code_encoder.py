class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        # Add virtual edges from node 0 to each house with cost equal to well cost
        for i in range(n):
            pipes.append([0, i + 1, wells[i]])
        # Sort pipes by cost
        pipes.sort(key=lambda x: x[2])

        parent = list(range(n + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                return True
            return False

        min_cost = 0
        for house1, house2, cost in pipes:
            if union(house1, house2):
                min_cost += cost

        return min_cost