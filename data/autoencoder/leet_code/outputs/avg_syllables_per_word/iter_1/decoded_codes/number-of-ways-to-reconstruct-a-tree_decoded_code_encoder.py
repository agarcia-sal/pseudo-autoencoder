from collections import defaultdict

def count_ways(pairs):
    graph = defaultdict(set)
    for u, v in pairs:
        graph[u].add(v)
        graph[v].add(u)

    n = len(graph)
    # find root = node with max degree
    root = max(graph, key=lambda x: len(graph[x]))
    if len(graph[root]) != n - 1:
        return 0

    def can_be_parent(u, v):
        # all neighbors of v are in neighbors[u] or equal to u itself
        return all(neigh in graph[u] or neigh == u for neigh in graph[v])

    ways = 1
    for u in graph:
        if u == root:
            continue
        candidates = []
        deg_u = len(graph[u])
        for v in graph[u]:
            deg_v = len(graph[v])
            if deg_v >= deg_u and can_be_parent(v, u):
                candidates.append((deg_v, v))
        if not candidates:
            return 0
        # pick parent with min degree
        parent_deg, parent = min(candidates)
        if parent_deg == deg_u:
            ways = 2

    return ways