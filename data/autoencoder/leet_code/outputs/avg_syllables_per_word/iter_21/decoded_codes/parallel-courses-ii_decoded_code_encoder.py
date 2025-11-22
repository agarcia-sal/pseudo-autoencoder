from collections import defaultdict, deque

class Solution:
    def minNumberOfSemesters(self, n, relations, k):
        graph, in_degree = self.initialize_graph_and_in_degree(n, relations)
        queue = self.initialize_queue(in_degree, n)
        semesters = 0

        while len(queue) > 0:
            courses_to_take = min(k, len(queue))
            for _ in range(courses_to_take):
                self.remove_and_process_course(queue, graph, in_degree)
            semesters += 1

        return semesters

    def initialize_graph_and_in_degree(self, n, relations):
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        for relation in relations:
            prevCourse = relation[0]
            nextCourse = relation[1]
            graph[prevCourse].append(nextCourse)
            in_degree[nextCourse] += 1
        return graph, in_degree

    def initialize_queue(self, in_degree, n):
        queue = deque()
        for course in range(1, n + 1):
            if in_degree[course] == 0:
                queue.append(course)
        return queue

    def remove_and_process_course(self, queue, graph, in_degree):
        current_course = queue.popleft()
        for next_course in graph[current_course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)