from collections import defaultdict, deque

class Solution:
    def minNumberOfSemesters(self, n, relations, k):
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)

        for prev_course, next_course in relations:
            graph[prev_course].append(next_course)
            in_degree[next_course] += 1

        queue = deque(course for course in range(1, n + 1) if in_degree[course] == 0)
        semesters = 0

        while queue:
            count = min(k, len(queue))
            for _ in range(count):
                current_course = queue.popleft()
                for next_course in graph[current_course]:
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)
            semesters += 1

        return semesters