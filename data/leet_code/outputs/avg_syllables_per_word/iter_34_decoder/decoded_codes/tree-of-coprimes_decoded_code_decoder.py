from math import gcd
from collections import defaultdict
from typing import List, Tuple, Optional

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # Precompute coprime relationships between values 1 to 50
        coprime = [[False] * 51 for _ in range(51)]
        for i in range(1, 51):
            for j in range(1, 51):
                coprime[i][j] = gcd(i, j) == 1

        result = [-1] * n
        ancestor_stack: List[Optional[Tuple[int, int]]] = [None] * 51  # stores (node, depth)

        def dfs(node: int, parent: int, depth: int) -> None:
            closest_ancestor = -1
            max_depth = -1
            node_val = nums[node]

            # Find closest ancestor with coprime value
            for val in range(1, 51):
                if coprime[node_val][val] and ancestor_stack[val] is not None:
                    anc_node, anc_depth = ancestor_stack[val]
                    if anc_depth > max_depth:
                        max_depth = anc_depth
                        closest_ancestor = anc_node

            result[node] = closest_ancestor

            # Update ancestor stack for current node's value
            original_ancestor = ancestor_stack[node_val]
            ancestor_stack[node_val] = (node, depth)

            for child in tree[node]:
                if child != parent:
                    dfs(child, node, depth + 1)

            # Restore ancestor stack state after returning from recursion
            ancestor_stack[node_val] = original_ancestor

        dfs(0, -1, 0)
        return result