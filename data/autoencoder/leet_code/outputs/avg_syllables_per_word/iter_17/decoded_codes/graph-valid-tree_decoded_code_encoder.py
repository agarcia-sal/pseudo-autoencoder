from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, number_of_nodes: int, list_of_edges: List[List[int]]) -> bool:
        if len(list_of_edges) != number_of_nodes - 1:
            return False

        adjacency_list = self.create_adjacency_list(number_of_nodes, list_of_edges)
        visited_nodes = set()

        def dfs(current_node: int) -> None:
            if current_node in visited_nodes:
                return
            visited_nodes.add(current_node)
            for neighbor in adjacency_list[current_node]:
                dfs(neighbor)

        dfs(0)
        return len(visited_nodes) == number_of_nodes

    def create_adjacency_list(self, number_of_nodes: int, list_of_edges: List[List[int]]) -> dict[int, List[int]]:
        adjacency_list = {i: [] for i in range(number_of_nodes)}
        for node_a, node_b in list_of_edges:
            adjacency_list[node_a].append(node_b)
            adjacency_list[node_b].append(node_a)
        return adjacency_list