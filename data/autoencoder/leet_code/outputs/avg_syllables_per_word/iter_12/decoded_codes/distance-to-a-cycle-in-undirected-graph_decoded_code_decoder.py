from collections import deque, defaultdict

class Solution:
    def distanceToCycle(self, n, edges):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent, path, visited):
            if node in visited:
                cycle_start = path.index(node)
                return path[cycle_start:]
            visited.add(node)
            path.append(node)
            for neighbor in graph[node]:
                if neighbor != parent:
                    cycle = dfs(neighbor, node, path, visited)
                    if cycle:
                        return cycle
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
            count = len(queue)
            for _ in range(count):
                node = queue.popleft()
                distance[node] = level
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            level += 1
        return distance