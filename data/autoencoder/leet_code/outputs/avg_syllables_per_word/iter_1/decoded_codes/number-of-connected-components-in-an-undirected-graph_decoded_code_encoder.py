def count_components(n, edges):
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()

    def dfs(node):
        if node not in visited:
            visited.add(node)
            for nbr in graph[node]:
                dfs(nbr)

    components = 0
    for node in range(n):
        if node not in visited:
            dfs(node)
            components += 1

    return components