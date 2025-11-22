class Solution:
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
        # Add virtual node 0 connected to each house with the cost of drilling a well
        for i in range(n):
            pipes.append([0, i + 1, wells[i]])

        # Sort edges by cost ascending
        pipes.sort(key=lambda x: x[2])

        parent = list(range(n + 1))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> bool:
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootX] = rootY
                return True
            return False

        min_cost = 0
        for _, house1, house2, cost in pipes:
            if union(house1, house2):
                min_cost += cost

        return min_cost