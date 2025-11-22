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

        # Precompute coprime pairs for values from 1 to 50 inclusive
        MAX_VAL = 50
        coprime = [[False]*(MAX_VAL+1) for _ in range(MAX_VAL+1)]
        for i in range(1, MAX_VAL+1):
            for j in range(1, MAX_VAL+1):
                coprime[i][j] = (gcd(i, j) == 1)

        result = [-1]*n
        # ancestor_stack[value] = Optional[Tuple[node, depth]] to record the closest ancestor with this value
        ancestor_stack: List[Optional[Tuple[int, int]]] = [None]*(MAX_VAL+1)

        def dfs(node: int, parent: int, depth: int) -> None:
            closest_ancestor = -1
            max_depth = -1
            current_val = nums[node]

            # For all possible values, check if coprime with current_val and if ancestor exists
            for val in range(1, MAX_VAL+1):
                if coprime[current_val][val]:
                    ancestor_info = ancestor_stack[val]
                    if ancestor_info is not None:
                        anc_node, anc_depth = ancestor_info
                        if anc_depth > max_depth:
                            max_depth = anc_depth
                            closest_ancestor = anc_node
            result[node] = closest_ancestor

            original_ancestor = ancestor_stack[current_val]
            ancestor_stack[current_val] = (node, depth)

            for child in tree[node]:
                if child != parent:
                    dfs(child, node, depth+1)

            ancestor_stack[current_val] = original_ancestor

        dfs(0, -1, 0)
        return result