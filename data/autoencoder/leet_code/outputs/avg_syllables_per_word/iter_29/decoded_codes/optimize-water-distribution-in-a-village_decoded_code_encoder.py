class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        # Add virtual edges connecting the virtual node 0 to each house with the cost of drilling a well
        for i in range(n):
            pipes.append([0, i + 1, wells[i]])
        # Sort all edges by cost
        pipes.sort(key=lambda x: x[2])

        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # Path compression
                x = parent[x]
            return x

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                return True
            return False

        min_cost = 0
        for house1, house2, cost in pipes:
            if union(house1, house2):
                min_cost += cost

        return min_cost