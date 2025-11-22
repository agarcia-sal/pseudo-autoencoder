from collections import deque, defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = defaultdict(list)
        in_degrees = [0] * numCourses

        for destination, source in prerequisites:
            adjacency_list[source].append(destination)
            in_degrees[destination] += 1

        queue = deque([course for course in range(numCourses) if in_degrees[course] == 0])
        topological_order = []

        while queue:
            current = queue.popleft()
            topological_order.append(current)
            for neighbor in adjacency_list[current]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(topological_order) == numCourses:
            return topological_order
        else:
            return []