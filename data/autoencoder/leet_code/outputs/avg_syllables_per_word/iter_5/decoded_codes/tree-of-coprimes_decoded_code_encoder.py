from math import gcd
from collections import defaultdict

class Solution:
    def getCoprimes(self, nums, edges):
        n = len(nums)
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        coprime = [[False]*51 for _ in range(51)]
        for i in range(1, 51):
            for j in range(1, 51):
                coprime[i][j] = (gcd(i, j) == 1)

        result = [-1] * n
        ancestor_stack = [None] * 51

        def dfs(node, parent, depth):
            closest_ancestor = -1
            max_depth = -1
            node_val = nums[node]
            for val in range(1, 51):
                if coprime[node_val][val] and ancestor_stack[val] is not None:
                    anc_node, anc_depth = ancestor_stack[val]
                    if anc_depth > max_depth:
                        max_depth = anc_depth
                        closest_ancestor = anc_node
            result[node] = closest_ancestor

            original_ancestor = ancestor_stack[node_val]
            ancestor_stack[node_val] = (node, depth)

            for child in tree[node]:
                if child != parent:
                    dfs(child, node, depth + 1)

            ancestor_stack[node_val] = original_ancestor

        dfs(0, -1, 0)
        return result