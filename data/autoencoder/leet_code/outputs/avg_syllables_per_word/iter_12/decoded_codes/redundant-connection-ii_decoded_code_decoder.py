from typing import List, Optional

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> Optional[List[int]]:
        def find(parent: List[int], i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent: List[int], rank: List[int], x: int, y: int) -> bool:
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
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        candidate1 = None
        candidate2 = None
        last = None

        # To detect a node with two parents
        parents = [0] * (n + 1)
        for u, v in edges:
            if parents[v] != 0:
                candidate1 = [parents[v], v]
                candidate2 = [u, v]
            else:
                parents[v] = u

        # If no node has two parents
        if candidate1 is None:
            for u, v in edges:
                if not union(parent, rank, u, v):
                    return [u, v]
            return None  # no redundant connection found (should not happen per problem constraints)

        # If a node has two parents, check for cycles
        # Reset DSU structure
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)
        for u, v in edges:
            if [u, v] == candidate2:
                continue
            if not union(parent, rank, u, v):
                return candidate1
        return candidate2