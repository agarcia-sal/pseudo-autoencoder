from collections import deque, defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        number_of_nodes = len(colors)
        graph = defaultdict(list)
        list_in_degree = [0] * number_of_nodes

        for origin_node, destination_node in edges:
            graph[origin_node].append(destination_node)
            list_in_degree[destination_node] += 1

        queue = deque(i for i in range(number_of_nodes) if list_in_degree[i] == 0)
        dp = [[0] * 26 for _ in range(number_of_nodes)]
        visited_nodes_count = 0
        maximum_color_value = 0

        while queue:
            current_node = queue.popleft()
            color_index = ord(colors[current_node]) - ord('a')
            dp[current_node][color_index] += 1
            maximum_color_value = max(maximum_color_value, dp[current_node][color_index])
            visited_nodes_count += 1

            for neighbor_node in graph[current_node]:
                for color_idx in range(26):
                    if dp[neighbor_node][color_idx] < dp[current_node][color_idx]:
                        dp[neighbor_node][color_idx] = dp[current_node][color_idx]
                list_in_degree[neighbor_node] -= 1
                if list_in_degree[neighbor_node] == 0:
                    queue.append(neighbor_node)

        return maximum_color_value if visited_nodes_count == number_of_nodes else -1