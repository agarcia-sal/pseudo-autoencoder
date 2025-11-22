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
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        candidate1: Optional[List[int]] = None
        candidate2: Optional[List[int]] = None
        last: Optional[List[int]] = None

        for u, v in edges:
            if parent[v] != v:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
            else:
                parent[v] = u
                if not union(parent, rank, u, v):
                    last = [u, v]

        if candidate1 is None:
            return last  # no node has two parents, so return last edge causing cycle
        if last is not None:
            return candidate1  # node with two parents and cycle
        return candidate2  # node with two parents but no cycle