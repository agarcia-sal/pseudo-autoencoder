from collections import deque, defaultdict
from typing import List

class Solution:
    def minNumberOfSemesters(self, number_of_courses: int, list_of_relations: List[List[int]], maximum_courses_per_semester: int) -> int:
        graph = defaultdict(list)
        in_degree = [0] * (number_of_courses + 1)

        for previous_course, next_course in list_of_relations:
            graph[previous_course].append(next_course)
            in_degree[next_course] += 1

        queue = deque()
        for course in range(1, number_of_courses + 1):
            if in_degree[course] == 0:
                queue.append(course)

        semesters = 0
        while queue:
            max_courses_this_semester = min(maximum_courses_per_semester, len(queue))
            for _ in range(max_courses_this_semester):
                current_course = queue.popleft()
                for next_course in graph[current_course]:
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)
            semesters += 1

        return semesters