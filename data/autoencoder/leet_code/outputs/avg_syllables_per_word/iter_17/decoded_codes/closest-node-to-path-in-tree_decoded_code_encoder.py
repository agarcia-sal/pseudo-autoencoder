from collections import defaultdict, deque
from math import inf

class Solution:
    def closestNode(self, n, edges, query):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def find_path(start, end):
            queue = deque([(start, [start])])
            visited = {start}
            while queue:
                current_node, current_path = queue.popleft()
                if current_node == end:
                    return current_path
                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current_path + [neighbor]))
            return []

        def closest_node_on_path(path, node):
            minimum_distance = inf
            closest_node = None
            for p in path:
                dist = len(find_path(p, node)) - 1
                if dist < minimum_distance:
                    minimum_distance = dist
                    closest_node = p
            return closest_node

        answer_list = []
        for start, end, node in query:
            current_path = find_path(start, end)
            answer_list.append(closest_node_on_path(current_path, node))
        return answer_list