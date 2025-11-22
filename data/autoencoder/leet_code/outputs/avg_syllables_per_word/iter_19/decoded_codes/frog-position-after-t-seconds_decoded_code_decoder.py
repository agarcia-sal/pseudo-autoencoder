from collections import defaultdict, deque

class Solution:
    def frogPosition(self, n, edges, t, target):
        if n == 1:
            return 1.0
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue = deque([(1, 1.0, 0)])
        visited = {1}
        while queue:
            curr_node, curr_prob, curr_time = queue.popleft()
            # If time reached or at a leaf (except node 1)
            if curr_time == t or (curr_node != 1 and len(graph[curr_node]) == 1):
                if curr_node == target:
                    return curr_prob
                continue
            possible_moves = len(graph[curr_node]) - (0 if curr_node == 1 else 1)
            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, curr_prob / possible_moves, curr_time + 1))
        return 0.0