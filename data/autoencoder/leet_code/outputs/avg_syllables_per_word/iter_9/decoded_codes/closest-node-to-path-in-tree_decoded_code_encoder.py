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

        def shortest_distance(a, b):
            if a == b:
                return 0
            q = deque([(a, 0)])
            visited = {a}
            while q:
                node, dist = q.popleft()
                for nei in graph[node]:
                    if nei == b:
                        return dist + 1
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, dist + 1))
            return float('inf')

        def closest_node_on_path(path, node):
            min_distance = float('inf')
            closest_node = None
            for p in path:
                dist = shortest_distance(p, node)
                if dist < min_distance:
                    min_distance = dist
                    closest_node = p
            return closest_node

        answer = []
        for start, end, node in query:
            path = find_path(start, end)
            answer.append(closest_node_on_path(path, node))
        return answer