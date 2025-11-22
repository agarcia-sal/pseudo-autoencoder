def max_top3_score(edges, scores):
    from collections import defaultdict
    graph = defaultdict(list)

    # Build graph: node -> top 3 (score, neighbor)
    for u, v in edges:
        graph[u].append((scores[v], v))
        graph[v].append((scores[u], u))

    for node in graph:
        graph[node].sort(reverse=True, key=lambda x: x[0])
        graph[node] = graph[node][:3]

    def distinct(a, b, c, d):
        return len({a, b, c, d}) == 4

    max_score = -1
    for u, v in edges:
        for s1, x in graph[u]:
            for s2, y in graph[v]:
                if distinct(x, y, u, v):
                    max_score = max(max_score, s1 + s2 + scores[u] + scores[v])

    return max_score