from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values, edges, maxTime):
        graph = defaultdict(list)
        for u, v, time_val in edges:
            graph[u].append((v, time_val))
            graph[v].append((u, time_val))

        visited = set()
        max_quality = 0

        def dfs(node, current_time, current_quality):
            nonlocal max_quality
            if node == 0:
                if current_quality > max_quality:
                    max_quality = current_quality

            for neighbor, time_val in graph[node]:
                if time_val <= current_time:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        dfs(neighbor, current_time - time_val, current_quality + values[neighbor])
                        visited.remove(neighbor)
                    else:
                        dfs(neighbor, current_time - time_val, current_quality)

        visited.add(0)
        dfs(0, maxTime, values[0])

        return max_quality