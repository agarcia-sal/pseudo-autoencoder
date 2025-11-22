from collections import defaultdict, deque

class Solution:
    def frogPosition(self, n, edges, t, target):
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
                continue

            moves = len(graph[node]) - (1 if node != 1 else 0)

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, prob / moves, time + 1))

        return 0.0