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
            max_prerequisite_time = 0
            for prevCourse in graph[course]:
                current_prerequisite_time = dfs(prevCourse)
                if current_prerequisite_time > max_prerequisite_time:
                    max_prerequisite_time = current_prerequisite_time
            memo[course] = max_prerequisite_time + time[course - 1]
            return memo[course]

        total_minimum_time = 0
        for course in range(1, n + 1):
            current_time = dfs(course)
            if current_time > total_minimum_time:
                total_minimum_time = current_time

        return total_minimum_time