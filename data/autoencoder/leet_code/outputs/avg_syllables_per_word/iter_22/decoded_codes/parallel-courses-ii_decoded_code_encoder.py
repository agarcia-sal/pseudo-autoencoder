from collections import deque, defaultdict

class Solution:
    def minNumberOfSemesters(self, n: int, relations: list[list[int]], k: int) -> int:
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)

        for prev_course, next_course in relations:
            graph[prev_course].append(next_course)
            in_degree[next_course] += 1

        queue = deque()
        for course in range(1, n + 1):
            if in_degree[course] == 0:
                queue.append(course)

        semesters = 0
        while queue:
            number_of_courses_to_take = min(k, len(queue))
            for _ in range(number_of_courses_to_take):
                current_course = queue.popleft()
                for next_course in graph[current_course]:
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)
            semesters += 1

        return semesters