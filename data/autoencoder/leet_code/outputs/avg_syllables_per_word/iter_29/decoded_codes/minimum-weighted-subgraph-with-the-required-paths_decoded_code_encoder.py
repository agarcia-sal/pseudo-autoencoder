import heapq
from typing import List, Tuple

class Solution:
    def minimumWeight(self, number_of_nodes: int, number_of_edges: List[Tuple[int, int, int]], 
                      source_node_one: int, source_node_two: int, destination_node: int) -> int:
        def dijkstra(graph: List[List[Tuple[int, int]]], start_node: int) -> List[int]:
            distances = [float('inf')] * number_of_nodes
            distances[start_node] = 0
            priority_queue = [(0, start_node)]

            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)
                if current_distance > distances[current_node]:
                    continue
                for neighbor, weight in graph[current_node]:
                    computed_distance = current_distance + weight
                    if computed_distance < distances[neighbor]:
                        distances[neighbor] = computed_distance
                        heapq.heappush(priority_queue, (computed_distance, neighbor))
            return distances

        graph = [[] for _ in range(number_of_nodes)]
        reverse_graph = [[] for _ in range(number_of_nodes)]

        for start_vertex, end_vertex, weight_value in number_of_edges:
            graph[start_vertex].append((end_vertex, weight_value))
            reverse_graph[end_vertex].append((start_vertex, weight_value))

        distances_from_source_one = dijkstra(graph, source_node_one)
        distances_from_source_two = dijkstra(graph, source_node_two)
        distances_to_destination = dijkstra(reverse_graph, destination_node)

        minimum_total_weight = float('inf')
        for i in range(number_of_nodes):
            d1, d2, d3 = distances_from_source_one[i], distances_from_source_two[i], distances_to_destination[i]
            if d1 != float('inf') and d2 != float('inf') and d3 != float('inf'):
                combined_distance = d1 + d2 + d3
                if combined_distance < minimum_total_weight:
                    minimum_total_weight = combined_distance

        return -1 if minimum_total_weight == float('inf') else minimum_total_weight