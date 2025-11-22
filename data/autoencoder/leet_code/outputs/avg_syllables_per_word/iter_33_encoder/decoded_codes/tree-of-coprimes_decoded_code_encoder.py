from collections import defaultdict
from math import gcd
from typing import List, Tuple, Optional

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # Precompute coprime matrix for values 1 to 50
        coprime = [[False] * 51 for _ in range(51)]
        for i in range(1, 51):
            for j in range(1, 51):
                coprime[i][j] = gcd(i, j) == 1

        result = [-1] * n
        ancestor_stack: List[Optional[Tuple[int, int]]] = [None] * 51

        def dfs(node: int, parent: int, depth: int) -> None:
            closest_ancestor = -1
            max_depth = -1
            val = nums[node]

            # Check all values 1..50 if they are coprime with current node's value and have ancestor
            for value in range(1, 51):
                if coprime[val][value] and ancestor_stack[value] is not None:
                    anc_node, anc_depth = ancestor_stack[value]
                    if anc_depth > max_depth:
                        max_depth = anc_depth
                        closest_ancestor = anc_node

            result[node] = closest_ancestor

            original_ancestor = ancestor_stack[val]
            ancestor_stack[val] = (node, depth)

            for child in tree[node]:
                if child != parent:
                    dfs(child, node, depth + 1)

            ancestor_stack[val] = original_ancestor

        dfs(0, -1, 0)
        return result