from collections import defaultdict, deque
from math import inf

class Solution:
    def closestNode(self, number_of_nodes, list_of_edges, list_of_queries):
        graph = defaultdict(list)
        for u, v in list_of_edges:
            graph[u].append(v)
            graph[v].append(u)

        def find_path(start_node, end_node):
            queue = deque([(start_node, [start_node])])
            visited_nodes = {start_node}
            while queue:
                node, path = queue.popleft()
                if node == end_node:
                    return path
                for neighbor in graph[node]:
                    if neighbor not in visited_nodes:
                        visited_nodes.add(neighbor)
                        queue.append((neighbor, path + [neighbor]))
            return []

        def closest_node_on_path(list_of_path_nodes, target_node):
            minimum_distance = inf
            closest_node_found = None
            for path_node in list_of_path_nodes:
                distance_to_node = len(find_path(path_node, target_node)) - 1
                if distance_to_node < minimum_distance:
                    minimum_distance = distance_to_node
                    closest_node_found = path_node
            return closest_node_found

        answer_list = []
        for start_value, end_value, node_value in list_of_queries:
            current_path = find_path(start_value, end_value)
            answer_list.append(closest_node_on_path(current_path, node_value))

        return answer_list