from collections import defaultdict
from typing import List

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        prereq_map = defaultdict(list)
        for prev_course, next_course in relations:
            prereq_map[next_course].append(prev_course)

        memo = [-1] * (n + 1)

        def dfs(course: int) -> int:
            if memo[course] != -1:
                return memo[course]
            max_prereq_time = 0
            for prev in prereq_map[course]:
                curr_time = dfs(prev)
                if curr_time > max_prereq_time:
                    max_prereq_time = curr_time
            memo[course] = max_prereq_time + time[course - 1]
            return memo[course]

        total_time = 0
        for course in range(1, n + 1):
            current_time = dfs(course)
            if current_time > total_time:
                total_time = current_time
        return total_time