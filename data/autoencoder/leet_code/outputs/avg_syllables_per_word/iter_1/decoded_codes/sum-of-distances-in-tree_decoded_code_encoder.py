def calculate_distances(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    count = [1] * n
    dist = [0] * n

    def dfs1(u, p):
        for v in adj[u]:
            if v != p:
                dfs1(v, u)
                count[u] += count[v]
                dist[u] += dist[v] + count[v]

    def dfs2(u, p):
        for v in adj[u]:
            if v != p:
                dist[v] = dist[u] - count[v] + (n - count[v])
                dfs2(v, u)

    dfs1(0, -1)
    dfs2(0, -1)
    return dist