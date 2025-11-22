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
            max_prerequisite_time = 0
            for prev_course in graph[course]:
                max_prerequisite_time = max(max_prerequisite_time, dfs(prev_course))
            memo[course] = max_prerequisite_time + time[course - 1]
            return memo[course]

        total_minimum_time = 0
        for course in range(1, n + 1):
            total_minimum_time = max(total_minimum_time, dfs(course))

        return total_minimum_time