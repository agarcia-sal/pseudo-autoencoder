from collections import defaultdict, deque

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
                node, path = queue.popleft()
                if node == end:
                    return path
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, path + [neighbor]))

        def closest_node_on_path(path, node):
            min_distance = float('inf')
            closest_node = None
            for p in path:
                distance = len(find_path(p, node)) - 1
                if distance < min_distance:
                    min_distance = distance
                    closest_node = p
            return closest_node

        answer = []
        for start, end, node in query:
            path = find_path(start, end)
            answer.append(closest_node_on_path(path, node))

        return answer