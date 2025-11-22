from collections import deque, defaultdict

def find_cycle_distances(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, parent, path, visited):
        if node in visited:
            # return cycle path starting from first occurrence of node
            idx = path.index(node)
            return path[idx:]
        visited.add(node)
        path.append(node)
        for neighbor in graph[node]:
            if neighbor != parent:
                c = dfs(neighbor, node, path, visited)
                if c:
                    return c
        path.pop()
        return None

    visited = set()
    cycle = None
    for node in range(n):
        if node not in visited:
            cycle = dfs(node, -1, [], visited)
            if cycle:
                break

    distance = [0] * n
    queue = deque(cycle)
    visited = set(cycle)
    level = 0
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            distance[node] = level
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        level += 1

    return distance