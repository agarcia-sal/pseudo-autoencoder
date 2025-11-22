def max_highway_cost(n, highways, k):
    graph = [[] for _ in range(n)]
    for u, v, toll in highways:
        graph[u].append((v, toll))
        graph[v].append((u, toll))

    max_cost = -1

    def dfs(city, visited, cost, used):
        nonlocal max_cost
        if used == k:
            max_cost = max(max_cost, cost)
            return
        for nbr, toll in graph[city]:
            if nbr not in visited:
                visited.add(nbr)
                dfs(nbr, visited, cost + toll, used + 1)
                visited.remove(nbr)

    for city in range(n):
        dfs(city, {city}, 0, 0)

    return max_cost