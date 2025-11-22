from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values, edges, maxTime):
        graph = defaultdict(list)
        for u, v, time in edges:
            graph[u].append((v, time))
            graph[v].append((u, time))

        visited = set([0])
        max_quality = 0

        def dfs(node, current_time, current_quality):
            nonlocal max_quality
            if node == 0:
                if current_quality > max_quality:
                    max_quality = current_quality
            for neighbor, time_cost in graph[node]:
                remaining_time = current_time - time_cost
                if remaining_time >= 0:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        dfs(neighbor, remaining_time, current_quality + values[neighbor])
                        visited.remove(neighbor)
                    else:
                        dfs(neighbor, remaining_time, current_quality)

        dfs(0, maxTime, values[0])
        return max_quality