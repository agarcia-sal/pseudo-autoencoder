from collections import defaultdict
from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        for prevCourse, nextCourse in relations:
            graph[nextCourse].append(prevCourse)

        memo = [-1] * (n + 1)

        def dfs(course: int) -> int:
            if memo[course] != -1:
                return memo[course]
            max_prereq_time = 0
            for prevCourse in graph[course]:
                candidate_time = dfs(prevCourse)
                if candidate_time > max_prereq_time:
                    max_prereq_time = candidate_time
            memo[course] = max_prereq_time + time[course - 1]
            return memo[course]

        total_minimum_time = 0
        for course in range(1, n + 1):
            course_time = dfs(course)
            if course_time > total_minimum_time:
                total_minimum_time = course_time

        return total_minimum_time