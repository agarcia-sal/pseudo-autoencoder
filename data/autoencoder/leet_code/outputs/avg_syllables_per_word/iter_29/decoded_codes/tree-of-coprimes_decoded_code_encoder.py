from math import gcd
from collections import defaultdict
from typing import List, Optional, Tuple


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        number_of_nodes = len(nums)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        coprime = [[False] * 51 for _ in range(51)]
        for i in range(1, 51):
            for j in range(1, 51):
                coprime[i][j] = (gcd(i, j) == 1)

        result = [-1] * number_of_nodes
        # ancestor_stack[value] = Optional[Tuple[node, depth]]
        ancestor_stack: List[Optional[Tuple[int, int]]] = [None] * 51

        def dfs(node: int, parent: int, depth: int) -> None:
            closest_ancestor = -1
            maximum_depth = -1
            node_val = nums[node]

            # Find closest ancestor whose value is coprime with current node's value
            for value in range(1, 51):
                if coprime[node_val][value] and ancestor_stack[value] is not None:
                    anc_node, anc_depth = ancestor_stack[value]
                    if anc_depth > maximum_depth:
                        maximum_depth = anc_depth
                        closest_ancestor = anc_node
            result[node] = closest_ancestor

            # Save the previous ancestor for this node's value before overriding
            original_ancestor = ancestor_stack[node_val]
            ancestor_stack[node_val] = (node, depth)

            for child in tree[node]:
                if child != parent:
                    dfs(child, node, depth + 1)

            # Restore original ancestor after exploring subtree
            ancestor_stack[node_val] = original_ancestor

        dfs(0, -1, 0)

        return result