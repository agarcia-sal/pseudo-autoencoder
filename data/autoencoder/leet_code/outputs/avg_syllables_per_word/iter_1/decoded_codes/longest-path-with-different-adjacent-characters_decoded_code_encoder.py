def longest_path(parent, s):
    from collections import defaultdict
    tree = defaultdict(list)
    for i in range(1, len(parent)):
        tree[parent[i]].append(i)

    result = 1

    def dfs(node):
        nonlocal result
        max1, max2 = 0, 0
        for child in tree[node]:
            length = dfs(child)
            if s[child] != s[node]:
                if length > max1:
                    max2 = max1
                    max1 = length
                elif length > max2:
                    max2 = length
        result = max(result, max1 + max2 + 1)
        return max1 + 1

    dfs(0)
    return result