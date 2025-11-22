from typing import List, Optional

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> Optional[List[int]]:
        def find(parent: List[int], i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent: List[int], rank: List[int], x: int, y: int) -> bool:
            root_x = find(parent, x)
            root_y = find(parent, y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1
                return True
            return False

        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        candidate1 = None
        candidate2 = None
        last = None

        # Track parents to detect a node with two parents
        parent_of = [0] * (n + 1)

        for u, v in edges:
            if parent_of[v] != 0:
                candidate1 = [parent_of[v], v]
                candidate2 = [u, v]
            else:
                parent_of[v] = u

        # Reset DSU for union calls
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        for u, v in edges:
            # Skip the second edge of the two-parent case
            if candidate2 is not None and [u, v] == candidate2:
                continue
            if not union(parent, rank, u, v):
                last = [u, v]

        if candidate1 is None:
            return last
        if last is not None:
            return candidate1
        return candidate2