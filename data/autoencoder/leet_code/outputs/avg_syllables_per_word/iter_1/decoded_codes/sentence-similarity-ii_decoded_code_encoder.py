def are_strings_similar(s1, s2, pairs):
    if len(s1) != len(s2):
        return False

    parent = dict()

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        parent.setdefault(x, x)
        parent.setdefault(y, y)
        parent[find(y)] = find(x)

    for x, y in pairs:
        union(x, y)

    for w1, w2 in zip(s1, s2):
        parent.setdefault(w1, w1)
        parent.setdefault(w2, w2)
        if find(w1) != find(w2):
            return False

    return True