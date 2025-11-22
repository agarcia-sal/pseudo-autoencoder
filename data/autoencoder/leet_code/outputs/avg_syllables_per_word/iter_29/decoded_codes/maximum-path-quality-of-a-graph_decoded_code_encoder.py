from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:
        graph_structure = defaultdict(list)
        for node_u, destination_node_v, travel_time in edges:
            graph_structure[node_u].append((destination_node_v, travel_time))
            graph_structure[destination_node_v].append((node_u, travel_time))

        visited_nodes = set()
        maximum_quality = 0

        def dfs(current_node: int, remaining_time: int, accumulated_quality: int):
            nonlocal maximum_quality
            if current_node == 0:
                maximum_quality = max(maximum_quality, accumulated_quality)

            for neighbor_node, travel_time in graph_structure[current_node]:
                if travel_time <= remaining_time:
                    if neighbor_node not in visited_nodes:
                        visited_nodes.add(neighbor_node)
                        dfs(neighbor_node, remaining_time - travel_time, accumulated_quality + values[neighbor_node])
                        visited_nodes.remove(neighbor_node)
                    else:
                        dfs(neighbor_node, remaining_time - travel_time, accumulated_quality)

        visited_nodes.add(0)
        dfs(0, maxTime, values[0])

        return maximum_quality