from collections import defaultdict
from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        for prev_course, next_course in relations:
            graph[next_course].append(prev_course)

        memo = [-1] * (n + 1)

        def dfs(course: int) -> int:
            if memo[course] != -1:
                return memo[course]

            max_prereq_time = 0
            for prev in graph[course]:
                curr_time = dfs(prev)
                if curr_time > max_prereq_time:
                    max_prereq_time = curr_time

            memo[course] = max_prereq_time + time[course - 1]
            return memo[course]

        total_min_time = 0
        for course in range(1, n + 1):
            curr_time = dfs(course)
            if curr_time > total_min_time:
                total_min_time = curr_time

        return total_min_time