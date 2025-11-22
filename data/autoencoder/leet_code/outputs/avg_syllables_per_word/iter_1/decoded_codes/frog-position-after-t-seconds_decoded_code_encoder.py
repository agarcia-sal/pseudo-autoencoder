from collections import deque, defaultdict

def frog_position(n, edges, t, target):
    if n == 1:
        return 1.0

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([(1, 1.0, 0)])
    visited = {1}

    while queue:
        node, prob, time = queue.popleft()

        if time == t or (node != 1 and len(graph[node]) == 1):
            if node == target:
                return prob
            else:
                continue

        moves = len(graph[node]) - (1 if node != 1 else 0)
        for nbr in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                queue.append((nbr, prob / moves, time + 1))

    return 0.0