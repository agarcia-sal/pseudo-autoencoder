from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values, edges, maxTime):
        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))

        max_quality = 0
        visited = set()

        def dfs(node, current_time, current_quality):
            nonlocal max_quality
            if node == 0:
                max_quality = max(max_quality, current_quality)
            for neighbor, t in graph[node]:
                if t <= current_time:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        dfs(neighbor, current_time - t, current_quality + values[neighbor])
                        visited.remove(neighbor)
                    else:
                        dfs(neighbor, current_time - t, current_quality)

        visited.add(0)
        dfs(0, maxTime, values[0])

        return max_quality