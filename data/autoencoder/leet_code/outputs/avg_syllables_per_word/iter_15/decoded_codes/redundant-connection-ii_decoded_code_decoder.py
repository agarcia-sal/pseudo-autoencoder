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

        # Check for nodes with two parents
        # `parent[v]` initially should be v; will be overwritten if a parent is assigned
        assigned_parent = [0] * (n + 1)
        for u, v in edges:
            if assigned_parent[v] != 0:
                candidate1 = [assigned_parent[v], v]
                candidate2 = [u, v]
            else:
                assigned_parent[v] = u

        # Initialize Union-Find for cycle detection
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)

        for u, v in edges:
            # If this edge is candidate2 (second parent edge), skip it first if candidate1 exists
            if candidate2 and [u, v] == candidate2:
                continue
            if not union(parent, rank, u, v):
                last = [u, v]

        if candidate1 is None:
            return last  # No node has two parents, just the last edge causing a cycle
        if last:
            return candidate1  # Two parents and a cycle => remove the first parent edge
        return candidate2  # Two parents but no cycle => remove the second parent edge