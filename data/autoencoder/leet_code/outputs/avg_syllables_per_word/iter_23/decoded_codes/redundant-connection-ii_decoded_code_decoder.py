from typing import List, Optional

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> Optional[List[int]]:
        def find(parent: List[int], index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent, parent[index])
            return parent[index]

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
                parent[v] = u
                # Re-initialize DSU parent for union-find
                # Because parent[v] is used for candidate detection,
                # we need separate parent for union-find.

        # For union-find operations, reset parent and rank
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        for u, v in edges:
            # If v has two parents, skip the second edge when checking union
            if candidate2 is not None and [u, v] == candidate2:
                continue
            if not union(parent, rank, u, v):
                last = [u, v]

        if candidate1 is None:
            return last
        if last is not None:
            return candidate1
        return candidate2