from math import gcd
from collections import defaultdict

def find_coprime_ancestors(nums, edges):
    n = len(nums)
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    coprime = [[gcd(i, j) == 1 for j in range(51)] for i in range(51)]

    result = [-1] * n
    ancestor_stack = [None] * 51

    def dfs(node, parent, depth):
        closest_ancestor, max_depth = -1, -1
        current_val = nums[node]

        for val in range(1, 51):
            if coprime[current_val][val] and ancestor_stack[val] is not None:
                anc, d = ancestor_stack[val]
                if d > max_depth:
                    closest_ancestor, max_depth = anc, d

        result[node] = closest_ancestor

        original = ancestor_stack[current_val]
        ancestor_stack[current_val] = (node, depth)

        for child in tree[node]:
            if child != parent:
                dfs(child, node, depth + 1)

        ancestor_stack[current_val] = original

    dfs(0, -1, 0)
    return result