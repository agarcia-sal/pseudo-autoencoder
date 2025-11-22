from collections import defaultdict, deque
from typing import List, Tuple

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[Tuple[int, int]]) -> bool:
        graph, indegree = self.initialize_graph_and_indegree(numCourses)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = self.initialize_queue_with_zero_indegree_courses(graph, indegree, numCourses)

        while queue:
            current_course = queue.popleft()
            numCourses -= 1

            for next_course in graph[current_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return numCourses == 0

    def initialize_graph_and_indegree(self, numCourses: int):
        graph = defaultdict(list)
        indegree = [0] * numCourses
        return graph, indegree

    def initialize_queue_with_zero_indegree_courses(self, graph, indegree, numCourses: int):
        return deque(course for course in range(numCourses) if indegree[course] == 0)