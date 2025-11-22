from typing import List

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # Add virtual edges from house 0 to each house (1 to n) with cost of well digging
        for i in range(n):
            pipes.append([0, i + 1, wells[i]])
        # Sort pipes by cost ascending
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
        for house1, house2, cost in pipes:
            if union(house1, house2):
                min_cost += cost

        return min_cost