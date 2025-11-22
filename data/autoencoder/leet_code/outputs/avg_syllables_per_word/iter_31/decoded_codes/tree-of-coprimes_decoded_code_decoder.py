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

        # Precompute coprime pairs for values 1 to 50
        max_val = 50
        coprime = [[False] * (max_val + 1) for _ in range(max_val + 1)]
        for i in range(1, max_val + 1):
            for j in range(1, max_val + 1):
                coprime[i][j] = gcd(i, j) == 1

        result = [-1] * n
        ancestor_stack: List[Optional[Tuple[int, int]]] = [None] * (max_val + 1)

        def dfs(node: int, parent: int, depth: int) -> None:
            closest_ancestor = -1
            max_depth = -1

            current_val = nums[node]
            for val in range(1, max_val + 1):
                if coprime[current_val][val]:
                    anc = ancestor_stack[val]
                    if anc is not None:
                        anc_node, anc_depth = anc
                        if anc_depth > max_depth:
                            max_depth = anc_depth
                            closest_ancestor = anc_node

            result[node] = closest_ancestor

            original_ancestor = ancestor_stack[current_val]
            ancestor_stack[current_val] = (node, depth)

            for child in tree[node]:
                if child != parent:
                    dfs(child, node, depth + 1)

            ancestor_stack[current_val] = original_ancestor

        dfs(0, -1, 0)
        return result