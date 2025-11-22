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

        for u, v in edges:
            if parent[v] != v:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
            else:
                parent[v] = u  # record parent for detecting two parents in directed graph
                if union(parent, rank, u, v) == False:
                    last = [u, v]

        if candidate1 is None:
            return last
        if last is not None:
            return candidate1
        return candidate2