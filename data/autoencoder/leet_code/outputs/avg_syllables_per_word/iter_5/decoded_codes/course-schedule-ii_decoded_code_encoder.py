from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj_list = [[] for _ in range(numCourses)]
        in_degrees = [0] * numCourses

        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degrees[dest] += 1

        queue = deque([i for i in range(numCourses) if in_degrees[i] == 0])
        topological_order = []

        while queue:
            current = queue.popleft()
            topological_order.append(current)

            for neighbor in adj_list[current]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return topological_order if len(topological_order) == numCourses else []