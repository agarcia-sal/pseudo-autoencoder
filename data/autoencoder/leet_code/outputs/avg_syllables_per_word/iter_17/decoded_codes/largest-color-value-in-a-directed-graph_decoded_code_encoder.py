from collections import deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        number_of_nodes = len(colors)

        # Initialize graph as adjacency list
        graph = [[] for _ in range(number_of_nodes)]
        # Initialize in-degree list
        in_degree_list = [0] * number_of_nodes

        for start_node, end_node in edges:
            graph[start_node].append(end_node)
            in_degree_list[end_node] += 1

        # Initialize queue with nodes having zero in-degree
        processing_queue = deque([node for node in range(number_of_nodes) if in_degree_list[node] == 0])
        # Initialize dp list, dp[node][color] = max count of 'color' up to this node
        dp_list = [[0] * 26 for _ in range(number_of_nodes)]

        visited_node_count = 0
        maximum_color_value = 0

        while processing_queue:
            current_node = processing_queue.popleft()
            color_index = ord(colors[current_node]) - ord('a')
            dp_list[current_node][color_index] += 1

            if dp_list[current_node][color_index] > maximum_color_value:
                maximum_color_value = dp_list[current_node][color_index]

            for adjacent_node in graph[current_node]:
                for color_idx in range(26):
                    if dp_list[current_node][color_idx] > dp_list[adjacent_node][color_idx]:
                        dp_list[adjacent_node][color_idx] = dp_list[current_node][color_idx]
                in_degree_list[adjacent_node] -= 1
                if in_degree_list[adjacent_node] == 0:
                    processing_queue.append(adjacent_node)

            visited_node_count += 1

        if visited_node_count == number_of_nodes:
            return maximum_color_value
        else:
            return -1