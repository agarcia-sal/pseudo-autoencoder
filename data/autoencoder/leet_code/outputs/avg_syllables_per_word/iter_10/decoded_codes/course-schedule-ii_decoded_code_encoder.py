from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj_list = self.createAdjacencyList(numCourses)
        in_degrees = self.createInDegreesList(numCourses)

        for dest, src in prerequisites:
            adj_list[src].append(dest)
            in_degrees[dest] += 1

        queue = deque(self.createQueue(numCourses, in_degrees))
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

    def createAdjacencyList(self, numCourses):
        return {i: [] for i in range(numCourses)}

    def createInDegreesList(self, numCourses):
        return [0] * numCourses

    def createQueue(self, numCourses, in_degrees):
        return [i for i in range(numCourses) if in_degrees[i] == 0]