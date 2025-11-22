def are_connected(n, threshold, queries):
    parent = list(range(n + 1))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[py] = px

    if threshold == 0:
        return [True] * len(queries)

    for i in range(threshold + 1, n + 1):
        for j in range(2 * i, n + 1, i):
            union(i, j)

    return [find(a) == find(b) for a, b in queries]