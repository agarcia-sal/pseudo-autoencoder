from collections import deque
from itertools import combinations

class Solution:
    def countSubgraphsForEachDiameter(self, n, edges):
        graph = {i: [] for i in range(1, n + 1)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(subtree):
            start = next(iter(subtree))
            queue = deque([start])
            visited = {start}
            farthest_node = start

            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei in subtree and nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
                        farthest_node = nei

            queue = deque([farthest_node])
            visited = {farthest_node}
            max_distance = 0

            while queue:
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()
                    for nei in graph[node]:
                        if nei in subtree and nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
                if queue:
                    max_distance += 1

            return max_distance

        result = [0] * (n - 1)

        for size in range(2, n + 1):
            for subset in combinations(range(1, n + 1), size):
                subset_set = set(subset)
                visited = set()
                stack = [subset[0]]
                while stack:
                    node = stack.pop()
                    if node not in visited:
                        visited.add(node)
                        for nei in graph[node]:
                            if nei in subset_set and nei not in visited:
                                stack.append(nei)
                if visited == subset_set:
                    diameter = bfs(subset_set)
                    if diameter > 0:
                        result[diameter - 1] += 1

        return result