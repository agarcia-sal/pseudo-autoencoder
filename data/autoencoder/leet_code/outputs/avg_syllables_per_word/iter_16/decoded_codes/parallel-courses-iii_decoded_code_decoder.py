from collections import defaultdict

class Solution:
    def minimumTime(self, n, relations, time):
        graph = defaultdict(list)
        for prev_course, next_course in relations:
            graph[next_course].append(prev_course)

        memo = [-1] * (n + 1)

        def dfs(course):
            if memo[course] != -1:
                return memo[course]
            max_prereq_time = 0
            for prev in graph[course]:
                candidate = dfs(prev)
                if candidate > max_prereq_time:
                    max_prereq_time = candidate
            memo[course] = max_prereq_time + time[course - 1]
            return memo[course]

        total_min_time = 0
        for course in range(1, n + 1):
            candidate = dfs(course)
            if candidate > total_min_time:
                total_min_time = candidate

        return total_min_time