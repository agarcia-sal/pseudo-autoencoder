from collections import defaultdict, deque
from typing import List

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        graph, in_degree = self.initializeGraph(n, relations)
        queue = self.initializeQueue(in_degree, n)
        semesters = 0

        while queue:
            courses_this_semester = min(k, len(queue))
            for _ in range(courses_this_semester):
                current_course = queue.popleft()
                for next_course in graph[current_course]:
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)
            semesters += 1

        return semesters

    def initializeGraph(self, n: int, relations: List[List[int]]):
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)

        for prevCourse, nextCourse in relations:
            graph[prevCourse].append(nextCourse)
            in_degree[nextCourse] += 1

        return graph, in_degree

    def initializeQueue(self, in_degree: List[int], n: int):
        queue = deque()
        for course in range(1, n + 1):
            if in_degree[course] == 0:
                queue.append(course)
        return queue