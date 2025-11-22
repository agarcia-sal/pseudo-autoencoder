from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj_list = defaultdict(list)
        in_degrees = [0] * numCourses

        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degrees[dest] += 1

        queue = deque([course for course in range(numCourses) if in_degrees[course] == 0])
        topological_order = []

        while queue:
            current = queue.popleft()
            topological_order.append(current)
            for neighbor in adj_list[current]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        return topological_order if len(topological_order) == numCourses else []