from collections import defaultdict, deque

class Solution:
    def minNumberOfSemesters(self, n: int, relations: list[list[int]], k: int) -> int:
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        for prevCourse, nextCourse in relations:
            graph[prevCourse].append(nextCourse)
            in_degree[nextCourse] += 1

        queue = deque()
        for course in range(1, n + 1):
            if in_degree[course] == 0:
                queue.append(course)

        semesters = 0
        while queue:
            limit = min(k, len(queue))
            for _ in range(limit):
                current_course = queue.popleft()
                for next_course in graph[current_course]:
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)
            semesters += 1

        return semesters