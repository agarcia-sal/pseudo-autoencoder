from typing import List

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # Add edges from the virtual node 0 to each house (1-indexed)
        for i in range(n):
            pipes.append([0, i + 1, wells[i]])

        # Sort pipes by their cost in ascending order
        pipes.sort(key=lambda x: x[2])

        parent = list(range(n + 1))  # parent array for union-find, including virtual node 0

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
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