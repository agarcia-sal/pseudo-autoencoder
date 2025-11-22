from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = [course for course in range(numCourses) if indegree[course] == 0]

        while queue:
            current_course = queue.pop(0)
            numCourses -= 1

            for next_course in graph[current_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return numCourses == 0