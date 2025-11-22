def find_critical_connections(n, connections):
    from collections import defaultdict

    G = defaultdict(list)
    for u, v in connections:
        G[u].append(v)
        G[v].append(u)

    disc = [-1] * n
    low = [-1] * n
    time = 0
    critical = []

    def dfs(u, p):
        nonlocal time
        disc[u], low[u] = time, time
        time += 1
        for v in G[u]:
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    critical.append([u, v])
            elif v != p:
                low[u] = min(low[u], disc[v])

    for u in range(n):
        if disc[u] == -1:
            dfs(u, -1)

    return critical