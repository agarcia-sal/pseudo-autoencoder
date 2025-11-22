def min_trio_degree(n, edges):
    graph = {i: set() for i in range(1, n+1)}
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    min_deg = float('inf')
    found = False

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if j not in graph[i]:
                continue
            for k in range(j+1, n+1):
                if k in graph[i] and k in graph[j]:
                    found = True
                    trio_deg = len(graph[i]) + len(graph[j]) + len(graph[k]) - 6
                    if trio_deg < min_deg:
                        min_deg = trio_deg

    return min_deg if found else -1