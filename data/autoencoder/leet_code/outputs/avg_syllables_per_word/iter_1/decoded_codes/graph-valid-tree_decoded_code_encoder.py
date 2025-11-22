def valid_tree(n, edges):
    if len(edges) != n - 1:
        return False
    adj = {i: [] for i in range(n)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    visited = set()
    def dfs(u):
        if u in visited:
            return
        visited.add(u)
        for v in adj[u]:
            dfs(v)
    dfs(0)
    return len(visited) == n