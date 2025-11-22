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

        for u, v in edges:
            # If v already has a parent different from itself, there's an edge causing two parents
            if parent[v] != v:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
            else:
                parent[v] = u

        # Reset union-find structure for cycle detection excluding candidate2 edge if exists
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        for u, v in edges:
            # Skip candidate2 edge temporarily if candidate2 exists, to check for cycle
            if candidate2 is not None and [u, v] == candidate2:
                continue
            if not union(parent, rank, u, v):
                # Found a cycle
                last = [u, v]

        if candidate1 is None:
            # No node had two parents, return the redundant edge causing the cycle
            return last if last is not None else []

        if last is not None:
            # Cycle detected after removing candidate2 edge, so candidate1 edge is redundant
            return candidate1

        # No cycle detected after removing candidate2 edge, so candidate2 edge is redundant
        return candidate2