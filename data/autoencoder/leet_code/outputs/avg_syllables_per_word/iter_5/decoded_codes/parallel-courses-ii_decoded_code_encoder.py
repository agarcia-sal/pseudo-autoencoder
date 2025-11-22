from collections import defaultdict, deque

class Solution:
    def minNumberOfSemesters(self, n, relations, k):
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)

        for prevCourse, nextCourse in relations:
            graph[prevCourse].append(nextCourse)
            in_degree[nextCourse] += 1

        queue = deque(course for course in range(1, n + 1) if in_degree[course] == 0)

        semesters = 0
        while queue:
            number_of_courses = min(k, len(queue))
            for _ in range(number_of_courses):
                current_course = queue.popleft()
                for next_course in graph[current_course]:
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)
            semesters += 1

        return semesters