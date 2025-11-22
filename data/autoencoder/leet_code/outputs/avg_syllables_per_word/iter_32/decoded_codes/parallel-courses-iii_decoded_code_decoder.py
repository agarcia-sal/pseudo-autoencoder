from typing import List, Dict

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph: Dict[int, List[int]] = {i: [] for i in range(1, n + 1)}
        for prev_course, next_course in relations:
            graph[next_course].append(prev_course)

        memo = [-1] * (n + 1)

        def dfs(course: int) -> int:
            if memo[course] != -1:
                return memo[course]

            max_prereq_time = 0
            for prev in graph[course]:
                candidate_time = dfs(prev)
                if candidate_time > max_prereq_time:
                    max_prereq_time = candidate_time

            memo[course] = max_prereq_time + time[course - 1]
            return memo[course]

        total_min_time = 0
        for course in range(1, n + 1):
            candidate_total_time = dfs(course)
            if candidate_total_time > total_min_time:
                total_min_time = candidate_total_time

        return total_min_time