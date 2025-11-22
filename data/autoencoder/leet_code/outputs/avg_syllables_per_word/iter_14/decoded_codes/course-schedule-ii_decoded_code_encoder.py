from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj_list = self.create_empty_adjacency_list(numCourses)
        in_degrees = self.create_zero_filled_list(numCourses)

        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degrees[dest] += 1

        queue = self.create_queue_with_courses(in_degrees, numCourses)
        topological_order = []

        while queue:
            current = queue.popleft()
            topological_order.append(current)

            for neighbor in adj_list[current]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(topological_order) == numCourses:
            return topological_order
        else:
            return []

    def create_empty_adjacency_list(self, numCourses):
        adjacency_list = {i: [] for i in range(numCourses)}
        return adjacency_list

    def create_zero_filled_list(self, length_value):
        return [0] * length_value

    def create_queue_with_courses(self, in_degrees, numCourses):
        result_queue = deque()
        for index in range(numCourses):
            if in_degrees[index] == 0:
                result_queue.append(index)
        return result_queue