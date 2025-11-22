from collections import defaultdict
from math import gcd
from typing import List

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        coprime = [[False] * 51 for _ in range(51)]
        for i in range(1, 51):
            for j in range(1, 51):
                coprime[i][j] = (gcd(i, j) == 1)

        result = [-1] * n
        ancestor_stack = [None] * 51  # Each entry: (node, depth) or None

        def dfs(node: int, parent: int, depth: int) -> None:
            closest_ancestor = -1
            max_depth = -1
            curr_val = nums[node]
            # Check all possible ancestor values for coprimality
            for val in range(1, 51):
                if coprime[curr_val][val]:
                    anc = ancestor_stack[val]
                    if anc is not None:
                        anc_node, anc_depth = anc
                        if anc_depth > max_depth:
                            max_depth = anc_depth
                            closest_ancestor = anc_node
            result[node] = closest_ancestor

            original_ancestor = ancestor_stack[curr_val]
            ancestor_stack[curr_val] = (node, depth)

            for child in tree[node]:
                if child != parent:
                    dfs(child, node, depth + 1)

            ancestor_stack[curr_val] = original_ancestor

        dfs(0, -1, 0)
        return result