from collections import defaultdict
from math import gcd
from typing import List, Optional

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def precompute_coprime_pairs() -> List[List[bool]]:
            coprime_matrix = [[False] * 51 for _ in range(51)]
            for i in range(1, 51):
                for j in range(1, 51):
                    coprime_matrix[i][j] = (gcd(i, j) == 1)
            return coprime_matrix

        coprime = precompute_coprime_pairs()

        result = [-1] * n
        ancestor_stack: List[Optional[tuple[int, int]]] = [None] * 51

        def dfs(node: int, parent: int, depth: int) -> None:
            closest_ancestor = -1
            max_depth = -1
            num_node = nums[node]

            for val in range(1, 51):
                if coprime[num_node][val] and ancestor_stack[val] is not None:
                    anc_node, anc_depth = ancestor_stack[val]
                    if anc_depth > max_depth:
                        max_depth = anc_depth
                        closest_ancestor = anc_node
            result[node] = closest_ancestor

            original_ancestor = ancestor_stack[num_node]
            ancestor_stack[num_node] = (node, depth)

            for child in tree[node]:
                if child != parent:
                    dfs(child, node, depth + 1)

            ancestor_stack[num_node] = original_ancestor

        dfs(0, -1, 0)

        return result