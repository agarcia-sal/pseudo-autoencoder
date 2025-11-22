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
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        candidate1 = None
        candidate2 = None
        last = None

        # For tracking actual parents for nodes to detect double parents
        actual_parent = [i for i in range(n + 1)]

        for u, v in edges:
            if actual_parent[v] != v:
                candidate1 = [actual_parent[v], v]
                candidate2 = [u, v]
            else:
                actual_parent[v] = u
                if not union(parent, rank, u, v):
                    last = [u, v]

        if candidate1 is None:
            return last

        if last is not None:
            return candidate1

        return candidate2