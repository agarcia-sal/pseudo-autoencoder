from typing import List, Optional

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
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
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        candidate1: Optional[List[int]] = None
        candidate2: Optional[List[int]] = None
        last: Optional[List[int]] = None

        # Used to track if a node has two parents
        parents = [0] * (n + 1)

        for u, v in edges:
            if parents[v] != 0:
                candidate1 = [parents[v], v]
                candidate2 = [u, v]
            else:
                parents[v] = u
                if not union(parent, rank, u, v):
                    last = [u, v]

        if candidate1 is None:
            return last if last is not None else []
        if last is not None:
            return candidate1
        return candidate2