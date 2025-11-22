from collections import deque
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        number_of_nodes = len(graph)
        queue = deque([[0]])
        answer_list = []
        while queue:
            path = queue.popleft()
            current_node = path[-1]
            if current_node == number_of_nodes - 1:
                answer_list.append(path)
                continue
            for neighbor_node in graph[current_node]:
                queue.append(path + [neighbor_node])
        return answer_list