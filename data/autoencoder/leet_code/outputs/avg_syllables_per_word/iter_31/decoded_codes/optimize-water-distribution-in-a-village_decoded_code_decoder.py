from typing import List

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        # Add a virtual node 0 with edges connecting to each house i (1-based),
        # cost is the well cost at house i.
        # To align with the pseudocode, houses are 1-indexed, and the virtual node is 0.
        for i in range(n):
            pipes.append([0, i + 1, wells[i]])

        # Sort pipes by cost ascending
        pipes.sort(key=lambda x: x[2])

        parent = list(range(n + 1))  # parent array for union-find, 0 to n inclusive

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

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