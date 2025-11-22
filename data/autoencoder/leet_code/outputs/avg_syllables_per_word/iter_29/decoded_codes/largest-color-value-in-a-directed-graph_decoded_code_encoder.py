from collections import deque, defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: List[str], edges: List[List[int]]) -> int:
        number_of_nodes = len(colors)
        graph = defaultdict(list)
        in_degree = [0] * number_of_nodes

        for current_node, adjacent_node in edges:
            graph[current_node].append(adjacent_node)
            in_degree[adjacent_node] += 1

        queue = deque(i for i in range(number_of_nodes) if in_degree[i] == 0)
        dp = [[0] * 26 for _ in range(number_of_nodes)]
        visited_nodes_count = 0
        maximum_color_value = 0

        while queue:
            current_node = queue.popleft()
            color_index = ord(colors[current_node]) - ord('a')
            dp[current_node][color_index] += 1
            if dp[current_node][color_index] > maximum_color_value:
                maximum_color_value = dp[current_node][color_index]
            visited_nodes_count += 1

            for adjacent_node in graph[current_node]:
                for color_i in range(26):
                    if dp[adjacent_node][color_i] < dp[current_node][color_i]:
                        dp[adjacent_node][color_i] = dp[current_node][color_i]
                in_degree[adjacent_node] -= 1
                if in_degree[adjacent_node] == 0:
                    queue.append(adjacent_node)

        if visited_nodes_count == number_of_nodes:
            return maximum_color_value
        else:
            return -1