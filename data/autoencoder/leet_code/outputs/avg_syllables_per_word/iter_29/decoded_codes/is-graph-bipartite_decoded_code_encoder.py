from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        number_of_nodes = len(graph)
        color_list = [0] * number_of_nodes

        def dfs(node: int, current_color: int) -> bool:
            color_list[node] = current_color
            for neighbor in graph[node]:
                if color_list[neighbor] == current_color:
                    return False
                if color_list[neighbor] == 0:
                    if not dfs(neighbor, -current_color):
                        return False
            return True

        for index in range(number_of_nodes):
            if color_list[index] == 0:
                if not dfs(index, 1):
                    return False
        return True