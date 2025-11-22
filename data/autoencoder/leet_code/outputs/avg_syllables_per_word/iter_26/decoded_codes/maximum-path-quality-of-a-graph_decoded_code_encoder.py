from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values, edges, maxTime):
        graph = defaultdict(list)
        for start_node, end_node, travel_time in edges:
            graph[start_node].append((end_node, travel_time))
            graph[end_node].append((start_node, travel_time))

        visited = set()
        max_quality = 0

        def dfs(node, current_time, current_quality):
            nonlocal max_quality
            if node == 0:
                max_quality = max(max_quality, current_quality)

            for neighbor_node, travel_time in graph[node]:
                if travel_time <= current_time:
                    if neighbor_node not in visited:
                        visited.add(neighbor_node)
                        dfs(neighbor_node, current_time - travel_time, current_quality + values[neighbor_node])
                        visited.remove(neighbor_node)
                    else:
                        dfs(neighbor_node, current_time - travel_time, current_quality)

        visited.add(0)
        dfs(0, maxTime, values[0])

        return max_quality