from collections import defaultdict

def solve(parents, nums):
    n = len(parents)
    tree = defaultdict(list)
    for i in range(1, n):
        tree[parents[i]].append(i)

    node_with_one = -1
    for i in range(n):
        if nums[i] == 1:
            node_with_one = i
            break
    if node_with_one == -1:
        return [1] * n

    result = [1] * n
    visited = set()

    def dfs(node):
        visited.add(node)
        vals = {nums[node]}
        for c in tree[node]:
            if c not in visited:
                vals |= dfs(c)
        miss = 1
        while miss in vals:
            miss += 1
        result[node] = miss
        return vals

    path = []
    cur = node_with_one
    while cur != -1:
        path.append(cur)
        cur = parents[cur]

    for node in reversed(path):
        if node not in visited:
            dfs(node)

    return result