from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):
        adjacency_list = {i: [] for i in range(numCourses)}
        in_degrees = [0] * numCourses

        for dest, src in prerequisites:
            adjacency_list[src].append(dest)
            in_degrees[dest] += 1

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