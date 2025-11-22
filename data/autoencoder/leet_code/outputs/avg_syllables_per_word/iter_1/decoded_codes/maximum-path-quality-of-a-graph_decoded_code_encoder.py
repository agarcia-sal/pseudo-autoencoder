def max_quality_path(edges, values, maxTime):
    graph = {}
    for u, v, t in edges:
        graph.setdefault(u, []).append((v, t))
        graph.setdefault(v, []).append((u, t))

    visited = set([0])
    max_quality = 0

    def dfs(node, time_left, quality):
        nonlocal max_quality
        if node == 0:
            max_quality = max(max_quality, quality)
        for nbr, t in graph.get(node, []):
            if t <= time_left:
                if nbr not in visited:
                    visited.add(nbr)
                    dfs(nbr, time_left - t, quality + values[nbr])
                    visited.remove(nbr)
                else:
                    dfs(nbr, time_left - t, quality)

    dfs(0, maxTime, values[0])
    return max_quality