from collections import defaultdict

class Solution:
    def minimumTime(self, n, relations, time):
        graph = defaultdict(list)
        for prevCourse, nextCourse in relations:
            graph[nextCourse].append(prevCourse)

        memo = [-1] * (n + 1)

        def dfs(course):
            if memo[course] != -1:
                return memo[course]

            max_prerequisite_time = 0
            for prevCourse in graph[course]:
                current_time = dfs(prevCourse)
                if current_time > max_prerequisite_time:
                    max_prerequisite_time = current_time

            memo[course] = max_prerequisite_time + time[course - 1]
            return memo[course]

        total_minimum_time = 0
        for course in range(1, n + 1):
            current_time = dfs(course)
            if current_time > total_minimum_time:
                total_minimum_time = current_time

        return total_minimum_time