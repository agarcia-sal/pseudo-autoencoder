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

        # Track parents of nodes to detect a node with two parents
        parent_map = [i for i in range(n + 1)]

        for u, v in edges:
            if parent_map[v] != v:
                candidate1 = [parent_map[v], v]
                candidate2 = [u, v]
            else:
                parent_map[v] = u

        # Reset Union-Find for actual cycle detection
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        for u, v in edges:
            # Skip the candidate2 edge if candidate1 exists (as candidate2 is the second edge causing indegree 2)
            if candidate2 and [u, v] == candidate2:
                continue
            if not union(parent, rank, u, v):
                last = [u, v]

        if not candidate1:
            return last  # no node with two parents, so cycle edge is redundant
        if last:
            return candidate1  # cycle detected, return the first edge causing two parents
        return candidate2  # no cycle, return second edge causing two parents