from collections import defaultdict, deque
from typing import List, Tuple, Dict

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1:
            return 1.0

        graph = self.BuildGraph(edges)
        queue = self.InitializeQueue()
        visited = self.InitializeVisited()

        # Enqueue starting position: node 1, probability 1.0, time 0
        self.Enqueue(1, 1.0, 0, queue, visited)

        while queue:
            current_node, current_prob, current_time = self.Dequeue(queue)

            # If time reached or the node is a leaf node (except node 1)
            if current_time == t or (current_node != 1 and len(graph[current_node]) == 1):
                if current_node == target:
                    return current_prob
                else:
                    continue

            # Number of unvisited neighbors (excluding the parent for non-root nodes)
            possible_moves = len(graph[current_node]) - (1 if current_node != 1 else 0)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    self.AddToVisited(neighbor, visited)
                    self.Enqueue(neighbor, current_prob / possible_moves, current_time + 1, queue, visited)

        return 0.0

    def BuildGraph(self, edges: List[List[int]]) -> Dict[int, List[int]]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def InitializeQueue(self) -> deque:
        return deque()

    def InitializeVisited(self) -> set:
        return {1}

    def Enqueue(self, node: int, current_prob: float, current_time: int, queue: deque, visited: set) -> None:
        queue.append((node, current_prob, current_time))

    def Dequeue(self, queue: deque) -> Tuple[int, float, int]:
        return queue.popleft()

    def AddToVisited(self, neighbor: int, visited: set) -> None:
        visited.add(neighbor)