from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

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
                candidate_time = dfs(prevCourse)
                if candidate_time > max_prerequisite_time:
                    max_prerequisite_time = candidate_time

            memo[course] = max_prerequisite_time + time[course - 1]
            return memo[course]

        total_minimum_time = 0
        for course in range(1, n + 1):
            candidate_time = dfs(course)
            if candidate_time > total_minimum_time:
                total_minimum_time = candidate_time

        return total_minimum_time